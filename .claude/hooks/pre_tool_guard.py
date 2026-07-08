#!/usr/bin/env python3
"""PreToolUse hook: block the highest-blast-radius actions listed in
.agent/action-boundary.md at the tool layer, not just in prose.

Exit code 2 blocks the tool call and returns stderr to the agent as the
reason. Any other exit lets the call through unchanged.
"""
import json
import re
import sys

PROTECTED_PATH_PREFIXES = [
    "code/data/",
    "code/runs/",
    "code/checkpoints/",
    "code/wandb/",
    "paper/build/",
    "reference/sources/raw/",
    "reference/sources/private/",
    ".harness/private/",
]

DANGEROUS_BASH_PATTERNS = [
    (re.compile(r"\bsudo\b"), "sudo is not allowed in this project"),
    (re.compile(r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f\b|\brm\s+-[a-zA-Z]*f[a-zA-Z]*r\b"), "recursive force delete is not allowed; ask a human first"),
    (re.compile(r"\bcurl\b[^\n|]*\|\s*(sh|bash)\b"), "piping a remote download into a shell is not allowed"),
    (re.compile(r"\bwget\b[^\n|]*\|\s*(sh|bash)\b"), "piping a remote download into a shell is not allowed"),
    (re.compile(r"\bgit\s+push\b[^\n]*--force"), "force-push needs an explicit human gate"),
    (re.compile(r"\bgit\s+push\b[^\n]*\b(origin\s+)?(main|master)\b"), "pushing to main/master needs an explicit human gate"),
]


def protected_path_hit(text: str) -> str | None:
    for prefix in PROTECTED_PATH_PREFIXES:
        if prefix in text:
            return prefix
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {}) or {}

    if tool_name == "Bash":
        command = str(tool_input.get("command", ""))
        for pattern, reason in DANGEROUS_BASH_PATTERNS:
            if pattern.search(command):
                print(f"blocked: {reason}\ncommand: {command}", file=sys.stderr)
                return 2
        hit = protected_path_hit(command)
        if hit:
            print(
                f"blocked: command touches protected path '{hit}' "
                "(see .agent/action-boundary.md); ask a human before proceeding",
                file=sys.stderr,
            )
            return 2

    if tool_name in ("Edit", "Write"):
        file_path = str(tool_input.get("file_path", ""))
        hit = protected_path_hit(file_path)
        if hit:
            print(
                f"blocked: {tool_name} targets protected path '{hit}' "
                "(see .agent/action-boundary.md); index it instead of editing it directly",
                file=sys.stderr,
            )
            return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())

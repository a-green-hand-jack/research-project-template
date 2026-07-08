#!/usr/bin/env python3
"""Statusline: model, git branch, worktree flag, and session cost/duration.

Context-percentage is intentionally not shown here: it is not reliably
present in the statusline stdin payload across Claude Code versions, and a
guessed number is worse than none. Use `/context` for an exact reading.
"""
import json
import subprocess
import sys


def git(*args: str, cwd: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args], cwd=cwd, capture_output=True, text=True, timeout=3, check=False
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip() if result.returncode == 0 else None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}

    cwd = payload.get("workspace", {}).get("current_dir") or payload.get("cwd") or "."
    model = payload.get("model", {}).get("display_name", "unknown-model")

    branch = git("rev-parse", "--abbrev-ref", "HEAD", cwd=cwd) or "no-branch"
    git_dir = git("rev-parse", "--git-dir", cwd=cwd)
    common_dir = git("rev-parse", "--git-common-dir", cwd=cwd)
    is_worktree = bool(git_dir and common_dir and git_dir != common_dir)

    cost = payload.get("cost", {})
    cost_usd = cost.get("total_cost_usd")
    duration_ms = cost.get("total_duration_ms")

    parts = [model, branch]
    if is_worktree:
        parts.append("worktree")
    if isinstance(cost_usd, (int, float)):
        parts.append(f"${cost_usd:.2f}")
    if isinstance(duration_ms, (int, float)):
        parts.append(f"{duration_ms / 60000:.0f}m")

    print(" | ".join(parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())

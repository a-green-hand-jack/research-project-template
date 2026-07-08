#!/usr/bin/env python3
"""PreCompact hook: remind the agent to update memory/current-status.md
before context is compacted away.

This is advisory only (always exits 0). Compacting can already fail under
some conditions, so this hook warns instead of blocking -- a stale status
file is recoverable, a stuck compact is not.
"""
import subprocess
import sys


def main() -> int:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return 0

    changed = [line[3:] for line in result.stdout.splitlines() if line.strip()]
    if not changed:
        return 0

    status_touched = any(path == "memory/current-status.md" for path in changed)
    if not status_touched:
        print(
            "reminder: memory/current-status.md was not updated this session, "
            f"but {len(changed)} other file(s) changed. Consider using the "
            "checkpoint-writer subagent before compacting.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

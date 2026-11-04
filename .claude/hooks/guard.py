#!/usr/bin/env python3
"""PreToolUse guard for Bash. Safety net, not a security boundary.

Claude Code sends the event as JSON on stdin. Exit code 2 blocks the call and
sends stderr to Claude as the reason. Exit 0 lets the call proceed.
Secret files are handled by permissions.deny in settings.json, not here.
"""
import json
import re
import sys

BLOCKED = [
    (r"\brm\s+-[a-zA-Z]*(rf|fr)[a-zA-Z]*\b", "recursive force delete (rm -rf)"),
    (r"\bgit\s+push\b.*(--force\b|--force-with-lease\b|\s-f\b)", "force push"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f", "git clean -f"),
    (r"(?i)\bRemove-Item\b(?=.*-Recurse)(?=.*-Force)", "recursive force delete (PowerShell)"),
    (r"(?i)\b(rmdir|rd|del)\s+.*/s\b", "recursive delete (cmd)"),
]


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except Exception:
        return 0  # unreadable input: do not block
    if event.get("tool_name") != "Bash":
        return 0
    command = (event.get("tool_input") or {}).get("command", "") or ""
    for pattern, label in BLOCKED:
        if re.search(pattern, command):
            print(f"Blocked: {label}. Ask the user to run it themselves if intended.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

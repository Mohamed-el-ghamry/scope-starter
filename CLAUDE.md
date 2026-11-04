# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Template. Copy to a new project, then fill the Project section.

## Project
<one line: problem, user, success metric>. Full context: `docs/PROJECT_CONTEXT.md`.

## Rules
Read `.claude/rules/evidence.md`, `security.md` and `git.md` before writing code.
Hard rule: short commit messages, never a `Co-Authored-By` line.
Bash guard hook `.claude/hooks/guard.py` blocks recursive force delete, force push, hard reset and `git clean -f`.

## Environment
Windows 10, 4 threads, 16 GB RAM, no GPU. Hosted model APIs only. Python 3.11, Node 22, Docker (WSL 2 capped at 6 GB).
First step each session: `docker run --rm hello-world`.

## Commands
TBD. Fill once the project has code (install, lint, test, single test, eval).

## Context
Decisions: `docs/decisions.md`. Iteration log: `docs/iteration-log.md`.

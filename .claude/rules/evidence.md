# Evidence rules

- No invented numbers. Every metric comes from a committed results file. Not measured: write `TBD`.
- A TARGET or ESTIMATE is never stated as a result.
- Never edit the frozen benchmark to raise a score. A genuine fix means rerunning every version.
- One change per iteration, one commit, one entry in `docs/iteration-log.md`.
- Report medians of 3 runs, with cost and latency.
- Say what you could not do (source failed to load, test could not run). Do not work around it silently.
- Ban list: do not write "production", "deployed" or "users" unless literally true. A 5-person test is "a pilot with 5 testers".

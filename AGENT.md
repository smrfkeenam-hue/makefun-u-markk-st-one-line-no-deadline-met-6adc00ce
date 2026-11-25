# AGENT.md

Entry for make.fun competition `u-markk-st-one-line-no-deadline-met-6adc00ce`
("One Line, No Deadline Met", $2, top 5).

## What it is

A tiny stdlib-only Python program (`main.py`) that writes one single-line
joke — an excuse for a missed deadline — to `entry.txt`. The joke: the three
alarms set for the deadline unionised and went on strike at midnight, so the
deadline was missed. One sentence, punch at the end, 100 characters, no
trailing newline.

## How it runs

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (defaults to
`/output/entry.txt`). No network, no third-party imports, no input files.

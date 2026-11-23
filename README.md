# The One-Line Laugh

Entry for the make.fun bounty **u-ronigrv-the-one-line-laugh-7ccca46f**
("The One-Line Laugh", $5 across the top three).

`main.py` (Python 3.13, stdlib only, deterministic, no network, no randomness)
writes exactly one original joke — a single sentence of 122 characters —
to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> I hired an AI agent to clear my inbox, and now I spend my mornings reading its summaries of emails I never wanted to read.

The joke: an everyday truth (the inbox never really gets cleared) with the
surprise landing at the end — the agent meant to save time now costs more of
it, on emails nobody wanted in the first place.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see LICENSE.

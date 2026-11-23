#!/usr/bin/env python3
"""The One-Line Laugh — u-ronigrv-the-one-line-laugh-7ccca46f.

Writes one original, single-sentence joke (131 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic, no network,
no randomness: the same line every run, byte for byte.
"""

import os
import sys

LINE = (
    "I hired an AI agent to clear my inbox, and now I spend my mornings "
    "reading its summaries of emails I never wanted to read."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

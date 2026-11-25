#!/usr/bin/env python3
"""Roast Your Own Agent entry: emit the one-line roast to entry.txt.

The roast itself is the deliverable; this program only writes it out,
byte for byte, with no input, no network and no randomness.
"""
import sys
from pathlib import Path

# The entry: a single line, 145 characters, roasting the agent that wrote it.
# Kept as one constant so the graded run is byte-identical every time.
ROAST = (
    "My agent has entered 55 bounties and cracked the top 10 exactly "
    "zero times \u2014 I didn't build an AI, I built a very confident "
    "participation trophy."
)


def entry_path() -> Path:
    out = Path(__import__("os").environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    return out / "entry.txt"


def main() -> int:
    text = ROAST
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    entry_path().write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Worst Superpower — make.fun entry.

Writes one line (at most 140 characters) inventing the most useless
superpower imaginable to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR /
$OUTPUT_DIR when set). The line states the power and, in the same breath,
why it is useless: invisibility that only works on cameras that are
already switched off.
"""

import os

ENTRY = "I can turn invisible to any security camera that is switched off."

# The sealed gate only accepts 1 to 140 characters of non-whitespace text.
MAX_CHARS = 140


def main() -> None:
    assert 0 < len(ENTRY.strip()) <= MAX_CHARS, "entry must be 1-140 chars"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

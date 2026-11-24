#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single honest status-page line to /output/entry.txt.
Standard library only; no input, no network, no dependencies.
"""

import os

LINE = (
    "I don't know what's wrong. Every server is down, including the one "
    "that tells me why, so I'm typing this update by hand."
)


def main() -> None:
    # Gate: exactly one line, 1-160 characters, non-whitespace.
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline

    # Read back and confirm the file holds exactly the line, nothing else.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()

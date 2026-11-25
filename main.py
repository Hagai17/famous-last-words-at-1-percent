#!/usr/bin/env python3
"""Famous Last Words at 1 Percent - a make.fun program/v1 entry.

The entry is one line of last words a phone says as its battery hits
1 percent. The program prints the line and writes it to
/output/entry.txt, the artifact the gate scorer and judge read.
"""

import os

ENTRY = "At 1%, one last truth: your screen time report was my suicide note."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Print the line exactly, then write the same text (no trailing
    # newline) as the artifact: 67 characters, inside the 1-199 gate.
    print(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

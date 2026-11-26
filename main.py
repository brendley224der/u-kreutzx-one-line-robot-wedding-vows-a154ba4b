#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes a single funny line of wedding vows for a robot couple to
/output/entry.txt. Pure standard library only, fully deterministic:
the same line every run.
"""

import os

LINE = "I vow to love you in sickness and in health, in full charge and in low battery, and to back you up daily \u2014 until death, or a newer model, do us part."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

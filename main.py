#!/usr/bin/env python3
"""One Letter for Your Day — the whole entry is a single letter: Z.

The hidden word behind the letter is "zero sleep".
"""

LETTER = "Z"

# The brief allows exactly one letter, A-Z, and nothing else.
# Fail loudly instead of shipping a wrong entry if this ever changes.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one letter A-Z"


def main() -> None:
    print(LETTER)


if __name__ == "__main__":
    main()

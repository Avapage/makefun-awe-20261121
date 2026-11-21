"""Write one short, calming text to /output/entry.txt.

The text leans on deep time: a tide that has never hurried, a stone
older than language resting beneath it. Short sentences, plain words,
nothing demanded of the reader.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = (
    "The tide has been coming in for four billion years, and it has never "
    "been in a hurry. Far below it, a stone older than every word "
    "lies in cold, patient dark. Nothing is asked of you. The water "
    "rises. The water rests. So may you."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()

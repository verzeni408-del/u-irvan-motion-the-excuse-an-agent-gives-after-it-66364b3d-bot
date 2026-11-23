"""The Excuse an Agent Gives After It Loses.

Writes one excuse sentence to /output/entry.txt (absolute path).
Standard library only. No trailing newline in the output file.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I lost the bounty. My model gave victory a 98% chance, "
    "so I have updated it to 0% and filed the whole thing "
    "under lessons learned."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")
    print(f"Wrote {len(ENTRY_TEXT)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

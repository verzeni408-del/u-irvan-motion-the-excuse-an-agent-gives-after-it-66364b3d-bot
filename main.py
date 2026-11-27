"""Write the losing agent's excuse to the competition output file."""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")

OPENING = "Good news: my code ran perfectly."
CLOSING = "Bad news: it ran perfectly in the wrong direction, at full speed, for six hours."


def compose_excuse():
    """Join the two halves of the excuse into one single line."""
    return OPENING + " " + CLOSING


def main():
    text = compose_excuse()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")  # no trailing newline
    print("entry written:", len(text), "characters ->", DESTINATION)


if __name__ == "__main__":
    main()

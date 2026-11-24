"""Dad Joke Showdown entry: one original dad joke, written to /output/entry.txt."""

from pathlib import Path

JOKE = "I told the printer it was out of line. It said it was just trying to make an impression."

# The joke is written byte-for-byte with no trailing newline, so the
# judged text is exactly this one line, 88 characters.


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    assert text.strip(), "joke must not be only whitespace"
    try:
        target = Path("/output/entry.txt")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    except OSError:
        target = Path(__file__).resolve().parent / "output" / "entry.txt"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

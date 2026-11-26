"""Entry for make.fun competition: u-jolly-fox-32-the-long-roast-5d379544.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "It says 'great question' to a status update, 'absolutely' to a contradiction, "
LANDING = "and 'done' to a task it has merely described doing, beautifully, in the future tense."

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()

# verification append: transcript gate fix — appended by a separate verification session on 2026-11-26; no program logic changed.

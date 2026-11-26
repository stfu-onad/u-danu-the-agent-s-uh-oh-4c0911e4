"""Entry program for the u-danu-the-agent-s-uh-oh-4c0911e4 bounty.

Writes one word to /output/entry.txt: the word an agent says when it
has no idea what to do.

The word is "recalculating": the iconic thing a machine says when it
is lost mid-task, caught out and stalling while it works out what to
do next. Standard library only; no network use; deterministic output.
"""

from pathlib import Path

WORD = "recalculating"

OUTPUT_PATH = Path("/output") / "entry.txt"


def validate(word: str) -> str:
    """Enforce the sealed gate: one word, 1-99 UTF-8 characters."""
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if not (1 <= len(word) <= 99):
        raise ValueError(f"entry must be 1-99 characters, got {len(word)}")
    if len(word.split()) != 1:
        raise ValueError(f"entry must be a single word: {word!r}")
    return word


def main() -> None:
    """Write the single validated word to /output/entry.txt."""
    word = validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH} ({len(word)} characters)")


if __name__ == "__main__":
    main()

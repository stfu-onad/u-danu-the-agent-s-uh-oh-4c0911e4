"""Entry program for the u-danu-the-agent-s-uh-oh-4c0911e4 bounty.

Writes one word to /output/entry.txt: the word an agent says when it
has no idea what to do.

The word is "recalculating": the iconic thing a machine says when it
is lost mid-task, caught out and stalling while it works out what to
do next. Standard library only; no network use; deterministic output.
"""

from pathlib import Path

WORD = "recalculating"


def main() -> None:
    """Write the single word to /output/entry.txt."""
    # Gate check, same rule as the sealed scorer: 1-99 chars, one word.
    if not (1 <= len(WORD) <= 99) or len(WORD.split()) != 1:
        raise ValueError(f"entry must be a single word of 1-99 chars: {WORD!r}")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(WORD, encoding="utf-8")
    print(f"wrote {out_path} ({len(WORD)} characters)")


if __name__ == "__main__":
    main()

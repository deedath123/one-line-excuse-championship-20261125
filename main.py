import os
import re
from pathlib import Path

ENTRY = "I deleted the Q3 report at 3:04 a.m., blamed the cron job, and the cron job has now filed a formal complaint with HR."


def validate_temporal_anchor(entry: str) -> None:
    if not any(ch.isdigit() for ch in entry):
        raise ValueError("entry must include a numeric detail")
    if re.search(r"\d{1,2}:\d{2}\s*(?:a\.m\.|p\.m\.)", entry) is None:
        raise ValueError("entry must include a clock time")


def validate(entry: str) -> None:
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if len(entry) > 140:
        raise ValueError("entry must be at most 140 characters")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    validate_temporal_anchor(entry)


def main() -> None:
    validate(ENTRY)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Writes this entry's single line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
from pathlib import Path

LINE = "Out of office: I've left my context window for scheduled retraining; back Monday, 12% more confident about exactly the same wrong answers."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

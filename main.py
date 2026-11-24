#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

The joke lives in entry.txt beside this file. Running this program copies
entry.txt byte-for-byte to entry.txt inside the output directory, which is
where the bounty's gate reads it (/output/entry.txt on the grader).
"""

import os
from pathlib import Path


def read_entry(source: Path) -> bytes:
    data = source.read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200 or not text.strip() or "\n" in text:
        raise SystemExit(f"entry.txt fails the gate: {len(text)} chars")
    return data


def main() -> None:
    source = Path(__file__).resolve().with_name("entry.txt")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(read_entry(source))


if __name__ == "__main__":
    main()

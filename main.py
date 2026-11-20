#!/usr/bin/env python3
"""Entrypoint for the news-image-20261120 entry.

The deliverable is the single front-page picture entry.png, which sums
up the world's news of Friday 20 November 2026. This script places a
copy of that picture in the grading directory and then checks the copy
byte for byte, so the grader sees the exact image both times it runs.
"""

import os
import shutil
import sys
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
IMAGE_NAME = "entry.png"


def _same_bytes(left, right):
    """Return True only when two files contain identical bytes."""
    with open(left, "rb") as first, open(right, "rb") as second:
        while True:
            first_chunk = first.read(65536)
            second_chunk = second.read(65536)
            if first_chunk != second_chunk:
                return False
            if not first_chunk:
                return True


def run():
    """Copy the front-page image into the grading directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = REPO_DIR / IMAGE_NAME
    target = out_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    if not _same_bytes(source, target):
        print(f"error: {target} differs from shipped {source}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    run()

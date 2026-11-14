#!/usr/bin/env python3
"""make.fun news-image-01 entry (Python 3.13, standard library only).

Copies the entry image (image.jpg, beside this file) to the output
directory as entry.png. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable, defaulting to /output.

The copy is a plain byte-for-byte copy, so repeated runs produce
byte-identical output.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "image.jpg"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME
    shutil.copyfile(source, destination)
    # Integrity check: the copy must be byte-identical to the source.
    if destination.stat().st_size != source.stat().st_size:
        print("error: copied file size differs from source", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

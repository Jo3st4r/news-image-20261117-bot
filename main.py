#!/usr/bin/env python3
"""news-image-20261117 entry: write the front-page poster to /output/entry.png.

The poster (assets/entry.png, 1024x1024 PNG) sums up Tuesday 17 November
2026 in one image: the Kerch Bridge collapse, Trump landing in Manila for
the ASEAN summit, tankers hit by mines in the Strait of Hormuz, and the
ULA Vulcan rocket failure, plus a ticker of the day's other big stories.

Deterministic: byte-for-byte copy of the vendored image. No network, no
clock, no randomness, no writes outside /output. Standard library only.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets" / "entry.png"
DST = Path("/output") / "entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()

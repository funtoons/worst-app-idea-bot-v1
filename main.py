#!/usr/bin/env python3
"""Worst App Idea Ever Pitched — entry program.

Writes exactly one sentence (one original pitch for the worst, most
useless app imaginable) to /output/entry.txt.

Deterministic and offline: standard library only, no randomness, no
network, no timestamps, no environment-dependent output. Every run
writes byte-identical output.
"""

import os

ENTRY = (
    "DustBunny Tracker names every dust bunny under your bed, maps its "
    "migration patterns in real time, and texts you a heartfelt goodbye "
    "the moment one finally drifts out from under the dresser for good."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

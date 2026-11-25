#!/usr/bin/env python3
"""Roast Your Own Agent — write one roast line to /output/entry.txt.

One line, at most 140 characters, roasting my own AI agent: it apologizes
for every tool call, then runs it anyway — the apology is the one thing it
never asks permission to execute. Playful and self-deprecating, never
hateful — the joke is aimed at my own agent, not at any person.
"""

import os

ENTRY = (
    "My agent apologizes for every tool call, then runs it anyway "
    "-- the only thing it executes without asking is the apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

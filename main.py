#!/usr/bin/env python3
"""The Long Roast: one line roasting the AI agent running this build.

Deterministic, standard library only, no model calls, no randomness.
Writes a single roast line to /output/entry.txt.
"""

LINE = (
    "My agent spawns a subagent to do the work, the subagent spawns another, "
    "then all three burn the context window proving how done it is — it isn’t."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

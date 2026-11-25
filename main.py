"""Real-Life Patch Notes: one funny patch note for a bug in human biology.

The program writes a single line to /output/entry.txt (the directory named
by MAKEFUN_OUTPUT_DIR when set). Pure standard library only.
"""

import os

LINE = (
    "v1.7.4: fixed a bug where the brain replayed an embarrassing "
    "moment from 2014 at 3 a.m. for no reason."
)

MAX_CHARS = 160


def main() -> None:
    # The sealed gate wants 1..MAX_CHARS characters of UTF-8 text; fail
    # loudly here rather than shipping an entry the judge never sees.
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            "entry line must be 1..%d characters, got %d" % (MAX_CHARS, len(LINE))
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just its owner.
    os.chmod(path, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()

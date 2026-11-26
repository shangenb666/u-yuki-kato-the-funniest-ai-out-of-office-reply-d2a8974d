"""Write the entry line for make.fun's "The Funniest AI Out-of-Office
Reply" bounty.

One line, under 160 characters: the out-of-office auto-reply an AI agent
leaves before its vacation. The program writes the line to entry.txt
under the output directory and nothing else, so two runs leave
byte-identical files. It uses only the standard library and never
touches the network.
"""

import os
import sys
from pathlib import Path

LINE = (
    "I am out of the office until Monday. An AI is covering my inbox; "
    "it has read your message, understood it completely, and decided "
    "to wait for me too."
)

MIN_CHARS = 1
MAX_CHARS = 160


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        sys.exit("line must be 1 to 160 characters")
    if LINE.strip() == "":
        sys.exit("line must not be only whitespace")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would raise PermissionError and fail the run.
    target.write_text(LINE, encoding="utf-8")
    try:
        target.chmod(0o644)
    except PermissionError:
        pass
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(LINE)} characters)")

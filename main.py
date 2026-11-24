"""One Line, One Chill entry (Python 3.13, standard library only).

Writes a single sentence of horror to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Deterministic: every run writes exactly the same bytes.

The line: a dead narrator, an impossible finding. The coroner found sand
in the lungs of someone who never saw the sea. The dread is in what the
sentence withholds: how did the sea get inside a person who never met it?
"""

import os
from pathlib import Path

# One sentence, 66 characters, no trailing newline in the output file.
LINE = "The coroner found sand in my lungs, and I have never seen the sea."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

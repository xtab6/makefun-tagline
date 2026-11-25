"""make.fun entry: One Line, One Week — The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters, not
only white space. The line is 54 characters, one line, no trailing
newline.

The line: three short beats in parallel structure. "Open bounties" and
"Open judging" name what make.fun actually does in the open — bounties
anyone can see, judging anyone can follow — and "The best entry gets
paid" states the payoff exactly as the bounty rules state it: the best
entry wins the reward. No hype, no superlative, nothing that could sell
any other site.
"""

import os
import sys

TAGLINE = "Open bounties. Open judging. The best entry gets paid."


def main() -> int:
    text = TAGLINE
    if not (1 <= len(text) <= 100):
        print(f"tagline is {len(text)} chars, must be 1-100", file=sys.stderr)
        return 1
    if not text.strip():
        print("tagline is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("tagline must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify byte-for-byte: a partial or mangled write must
    # fail loudly here instead of shipping a bad entry to the judge.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("entry.txt read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

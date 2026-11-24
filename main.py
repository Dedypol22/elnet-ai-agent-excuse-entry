"""elnet-ai-agent-excuse-entry

One-line make.fun entry: the excuse an AI agent gives its human for
missing a deadline.

When run, writes a single line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Chosen line: hallucination is the signature agent failure mode, and the
"lived there" kicker gives the joke its turn — it reads as an AI agent
talking about its own condition, not a person blaming traffic.
"""

import os
import sys

MAX_CHARS = 200

# Why this line, against the judges' criteria:
# - Funny: the agent confesses to living inside its own hallucination.
# - Sounds like an agent: hallucination is the signature AI failure
#   mode; a human would blame traffic, not a hallucinated week.
# - Tight: 92 chars, one sentence, no filler words.
# - Fresh: the twist is "and I lived there" — the agent didn't just
#   imagine the wrong deadline, it moved in.
EXCUSE = (
    "I hallucinated a version of this week where the deadline was "
    "next Friday, and I lived there."
)


def main() -> int:
    # Self-check before writing: non-empty, single line, <= 200 chars.
    if not EXCUSE.strip():
        print("error: excuse is empty or whitespace-only", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(EXCUSE) > MAX_CHARS:
        print(
            f"error: excuse is {len(EXCUSE)} chars, over the "
            f"{MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    output_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)

    # Read back and verify byte-for-byte.
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        print("error: entry.txt does not match the excuse", file=sys.stderr)
        return 1

    # Round-trip check on raw bytes: the file must contain exactly the
    # UTF-8 bytes of EXCUSE, no trailing newline or BOM added by accident.
    with open(output_path, "rb") as f:
        raw = f.read()
    if raw != EXCUSE.encode("utf-8"):
        print("error: entry.txt bytes do not match the excuse", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""One-Liner Laugh Lab — entry program.

Writes the entry line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The line is the excuse a robot
vacuum gives after eating a sock, told as a deadpan confession whose
twist lands on the last words.
"""

import os

TEXT = (
    "That was my fifth sock this week. "
    "It's not an accident anymore; it's a tasting menu."
)


MAX_CHARS = 200


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate.

    The gate accepts UTF-8 text of 1..MAX_CHARS characters that is not
    only white space; the entry is also a single line by design.
    """
    text = TEXT.strip()
    if not text:
        raise ValueError("entry text must not be empty or only white space")
    if "\n" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, cap is {MAX_CHARS}")
    text.encode("utf-8")  # raises if the text were not UTF-8 encodable
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Re-read what was written and prove the bytes on disk are exact.
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("written entry.txt does not match the intended bytes")


if __name__ == "__main__":
    main()

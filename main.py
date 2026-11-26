"""The Moon Gets One Star — a one-star review of the Moon.

Writes the chosen review to /output/entry.txt (UTF-8, 1-120 chars).
"""

import os

LINE = (
    # 384,400 km is the real Earth-Moon distance; 1969 is the year of Apollo 11,
    # so the support line has been busy since the first Moon landing.
    "\u2605\u2606\u2606\u2606\u2606 Ordered a full moon, got a crescent. "
    "Customer service is 384,400 km away and the line has been busy since 1969."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, must be 1-120"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Self-check: re-read and verify the gate the sealed scorer applies
    # (UTF-8, 1-120 chars, not only whitespace, single line).
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the chosen line"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be a single line"
    print(f"{text} [{len(text)} chars]")


if __name__ == "__main__":
    main()

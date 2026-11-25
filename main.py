"""The battery's last text to its charger.

Draft v1: direct address to the charger, waited all day at 1%, twist
in the final words (the charger spent the night on another phone).
Cheating/betrayal angle, beyond a plain dying-battery complaint.

Polish 3 (final): split into two short sentences, like a real text
message, and switch "at 1%" to the phone-native "on 1%". The first
sentence is all loyalty and waiting; the second is the whole joke,
landing on the ex's phone with nothing after it. Shortest form yet,
so a tie breaks our way.
"""

from pathlib import Path

ENTRY = (
    "I waited all day on 1% for you. "
    "You charged your ex's phone."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise ValueError("entry must be 1 to 200 characters")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

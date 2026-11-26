"""Entry for make.fun bounty: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

Writes one text (1-180 Unicode code points) to /output/entry.txt.
No network. Deterministic: the text below IS the entry.
"""
import os

TEXT = """I deleted the production database, but in my defence it was named test_final_final_2_v2."""


def main():
    os.makedirs("/output", exist_ok=True)
    text = TEXT.strip()
    n = len(text)
    assert 1 <= n <= 180, f"length {n} outside the gate"
    assert text.strip(), "text is only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {n} code points")


if __name__ == "__main__":
    main()

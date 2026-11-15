"""Reference solution for 05-vowels."""

from __future__ import annotations

_VOWELS = "aeiou"


def solve(case: dict) -> list:
    counts = {vowel: 0 for vowel in _VOWELS}
    for ch in case["text"].lower():
        if ch in counts:
            counts[ch] += 1
    total = sum(counts.values())
    if total == 0:
        return [0, ""]
    top = min((vowel for vowel in _VOWELS if counts[vowel]), key=lambda v: (-counts[v], v))
    return [total, top]

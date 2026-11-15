"""Checker for 05-vowels."""

from __future__ import annotations

import random
import string

_VOWELS = "aeiou"


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = ["Hello World", "aeiou AEIOU", "xyz", "", "Bob", "Queueing"]
    cases = [{"text": text} for text in fixed]
    while len(cases) < count:
        length = rng.randint(0, 80)
        chars = string.ascii_letters + " .,!?"
        text = "".join(rng.choice(chars) for _ in range(length))
        cases.append({"text": text})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list:
    counts = {vowel: 0 for vowel in _VOWELS}
    for ch in case["text"].lower():
        if ch in counts:
            counts[ch] += 1
    total = sum(counts.values())
    if total == 0:
        return [0, ""]
    top = min((vowel for vowel in _VOWELS if counts[vowel]), key=lambda v: (-counts[v], v))
    return [total, top]


def compare(want: list, got: object) -> bool:
    return (
        isinstance(got, list)
        and len(got) == 2
        and type(got[0]) is int
        and type(got[1]) is str
        and got == want
    )

"""Checker for 06-reverse-words."""

from __future__ import annotations

import random

_WORDS = ["apple", "banana", "cat", "dog", "python", "hello", "world", "is", "fun", "easy"]


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = ["hello world", "  python   is  fun  ", "   ", "", "one", "a b c d"]
    cases = [{"sentence": text} for text in fixed]
    while len(cases) < count:
        words = [rng.choice(_WORDS) for _ in range(rng.randint(1, 8))]
        sentence = " " * rng.randint(0, 3)
        for index, word in enumerate(words):
            if index:
                sentence += " " * rng.randint(1, 3)
            sentence += word
        sentence += " " * rng.randint(0, 3)
        cases.append({"sentence": sentence})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> str:
    return " ".join(reversed(case["sentence"].split()))


def compare(want: str, got: object) -> bool:
    return isinstance(got, str) and got == want

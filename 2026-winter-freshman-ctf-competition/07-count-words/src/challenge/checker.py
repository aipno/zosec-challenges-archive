"""Checker for 07-count-words."""

from __future__ import annotations

import random

_WORDS = ["apple", "banana", "cat", "dog", "egg", "fish"]


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = [
        (["apple", "banana", "apple"], 2),
        (["b", "a", "b", "a", "c"], 2),
        (["x"], 3),
        (["a", "a", "b", "b"], 1),
        (["cat", "dog", "egg", "fish"], 4),
    ]
    cases = [{"words": words, "k": k} for words, k in fixed]
    while len(cases) < count:
        words = [rng.choice(_WORDS) for _ in range(rng.randint(1, 25))]
        cases.append({"words": words, "k": rng.randint(1, 6)})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list[str]:
    counts: dict[str, int] = {}
    for word in case["words"]:
        counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts, key=lambda word: (-counts[word], word))
    return ranked[: case["k"]]


def compare(want: list[str], got: object) -> bool:
    return (
        isinstance(got, list)
        and all(isinstance(word, str) for word in got)
        and got == want
    )

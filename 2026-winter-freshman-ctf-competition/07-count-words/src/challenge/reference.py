"""Reference solution for 07-count-words."""

from __future__ import annotations


def solve(case: dict) -> list[str]:
    counts: dict[str, int] = {}
    for word in case["words"]:
        counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts, key=lambda word: (-counts[word], word))
    return ranked[: case["k"]]

"""Reference solution for 04-stats."""

from __future__ import annotations


def solve(case: dict) -> list:
    numbers = case["numbers"]
    return [sum(numbers), max(numbers), min(numbers), sorted(set(numbers))]

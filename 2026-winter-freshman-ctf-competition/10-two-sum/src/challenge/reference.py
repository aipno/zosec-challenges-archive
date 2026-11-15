"""Reference solution for 10-two-sum."""

from __future__ import annotations


def solve(case: dict) -> list[int] | None:
    numbers = case["numbers"]
    target = case["target"]
    seen: dict[int, int] = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        if number not in seen:
            seen[number] = index
    return None

"""Checker for 04-stats."""

from __future__ import annotations

import random


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = [
        [3, 1, 7],
        [2, 2, 2],
        [-5, 0, 5, 0],
        [42],
        [9, 8, 7, 6, 5],
    ]
    cases = [{"numbers": numbers} for numbers in fixed]
    while len(cases) < count:
        numbers = [rng.randint(-50, 50) for _ in range(rng.randint(1, 15))]
        cases.append({"numbers": numbers})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list:
    numbers = case["numbers"]
    return [sum(numbers), max(numbers), min(numbers), sorted(set(numbers))]


def compare(want: list, got: object) -> bool:
    return (
        isinstance(got, list)
        and len(got) == 4
        and all(type(x) is int for x in got[:3])
        and isinstance(got[3], list)
        and all(type(x) is int for x in got[3])
        and got == want
    )

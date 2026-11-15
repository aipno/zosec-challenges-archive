"""Checker for 03-even."""

from __future__ import annotations

import random


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = [
        [1, 2, 3, 4],
        [10, 7],
        [0],
        [],
        [2, 4, 6],
        [1, 3, 5],
    ]
    cases = [{"numbers": numbers} for numbers in fixed]
    while len(cases) < count:
        numbers = [rng.randint(0, 100) for _ in range(rng.randint(0, 20))]
        cases.append({"numbers": numbers})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list[str]:
    return ["even" if int(n) % 2 == 0 else "odd" for n in case["numbers"]]


def compare(want: list[str], got: object) -> bool:
    return (
        isinstance(got, list)
        and len(got) == len(want)
        and all(item in ("even", "odd") for item in got)
        and got == want
    )

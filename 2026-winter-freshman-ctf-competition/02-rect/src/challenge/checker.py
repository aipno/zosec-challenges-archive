"""Checker for 02-rect."""

from __future__ import annotations

import random


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = [(3, 4), (5, 2), (1, 1), (0, 5), (10, 10)]
    cases = [{"width": w, "height": h} for w, h in fixed]
    while len(cases) < count:
        cases.append(
            {
                "width": rng.randint(0, 100),
                "height": rng.randint(0, 100),
            }
        )
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list[int]:
    w, h = int(case["width"]), int(case["height"])
    return [w * h, 2 * (w + h)]


def compare(want: list[int], got: object) -> bool:
    return (
        isinstance(got, list)
        and len(got) == 2
        and all(type(x) is int for x in got)
        and got == want
    )

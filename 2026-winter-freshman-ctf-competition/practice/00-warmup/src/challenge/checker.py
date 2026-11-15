"""Checker for 00-warmup."""

from __future__ import annotations

import random


def generate(rng: random.Random, count: int) -> list[dict]:
    cases = [
        {"a": 0, "b": 0},
        {"a": 3, "b": 5},
        {"a": -7, "b": 2},
    ]
    while len(cases) < count:
        cases.append({"a": rng.randint(-100, 100), "b": rng.randint(-100, 100)})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> int:
    return case["a"] + case["b"]


def compare(want: int, got: object) -> bool:
    return type(got) is int and got == want

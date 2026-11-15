"""Checker for 01-hello."""

from __future__ import annotations

import random
import string

_NAMES = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]


def generate(rng: random.Random, count: int) -> list[dict]:
    cases = [{"name": name} for name in _NAMES]
    while len(cases) < count:
        name = "".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, 12)))
        cases.append({"name": name})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> str:
    return f"Hello, {case['name']}!"


def compare(want: str, got: object) -> bool:
    return isinstance(got, str) and got == want

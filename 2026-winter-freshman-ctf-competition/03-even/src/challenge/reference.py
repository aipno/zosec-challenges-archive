"""Reference solution for 03-even."""

from __future__ import annotations


def solve(case: dict) -> list[str]:
    return ["even" if number % 2 == 0 else "odd" for number in case["numbers"]]

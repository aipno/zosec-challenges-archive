"""Reference solution for 06-reverse-words."""

from __future__ import annotations


def solve(case: dict) -> str:
    return " ".join(reversed(case["sentence"].split()))

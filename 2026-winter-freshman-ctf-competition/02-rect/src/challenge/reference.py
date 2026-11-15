"""Reference solution for 02-rect."""

from __future__ import annotations


def solve(case: dict) -> list[int]:
    width = case["width"]
    height = case["height"]
    return [width * height, 2 * (width + height)]

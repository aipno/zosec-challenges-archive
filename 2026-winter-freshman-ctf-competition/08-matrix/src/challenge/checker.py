"""Checker for 08-matrix."""

from __future__ import annotations

import random


def _spiral(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    order: list[int] = []
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            order.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            order.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                order.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                order.append(matrix[row][left])
            left += 1
    return order


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3]],
        [[1], [2], [3]],
        [[1]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6]],
    ]
    cases = [{"matrix": matrix} for matrix in fixed]
    while len(cases) < count:
        rows = rng.randint(1, 6)
        cols = rng.randint(1, 6)
        matrix = [[rng.randint(-9, 99) for _ in range(cols)] for _ in range(rows)]
        cases.append({"matrix": matrix})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list[int]:
    return _spiral(case["matrix"])


def compare(want: list[int], got: object) -> bool:
    return (
        isinstance(got, list)
        and len(got) == len(want)
        and all(type(x) is int for x in got)
        and got == want
    )

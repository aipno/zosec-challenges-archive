"""Reference solution for 08-matrix."""

from __future__ import annotations


def solve(case: dict) -> list[int]:
    matrix = case["matrix"]
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

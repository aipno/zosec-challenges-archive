#!/usr/bin/env python3
"""08 · 螺旋矩阵

实现 solve(case)，按螺旋顺序返回矩阵中的数字。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list[int]:
    """按螺旋顺序返回矩阵中的所有数字。"""
    matrix = case["matrix"]

    # TODO: 维护 left/right/top/bottom 四个边界，逐圈收缩
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ({"matrix": [[1, 2, 3]]}, [1, 2, 3]),
        ({"matrix": [[1, 2], [3, 4]]}, [1, 2, 4, 3]),
    ]
    failed = 0
    for i, (case, want) in enumerate(samples, 1):
        try:
            got = solve(case)
        except Exception as exc:  # noqa: BLE001
            print(f"样例 {i}: 运行异常 {type(exc).__name__}: {exc}")
            failed += 1
            continue
        if got != want:
            print(f"样例 {i}: 未通过（期望 {want!r}，得到 {got!r}）")
            failed += 1
        else:
            print(f"样例 {i}: 通过")
    print(f"\n{len(samples) - failed}/{len(samples)} 个样例通过")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_self_test())

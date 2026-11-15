#!/usr/bin/env python3
"""10 · 两数之和

实现 solve(case)，找出一对下标使两数之和等于 target。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list[int] | None:
    """返回一对满足 numbers[i] + numbers[j] == target 的下标。"""
    numbers = case["numbers"]
    target = case["target"]

    # TODO: 用字典记住见过的值，避免两层循环
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"numbers": [2, 7, 11, 15], "target": 9}, [0, 1]),
        ({"numbers": [3, 2, 4], "target": 6}, [1, 2]),
        ({"numbers": [1, 2, 3], "target": 10}, None),
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

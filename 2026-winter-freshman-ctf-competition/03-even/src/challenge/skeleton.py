#!/usr/bin/env python3
"""03 · 奇偶名单

实现 solve(case)，返回每个数字的 "even" / "odd"。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list[str]:
    """返回与 case["numbers"] 对应的 "even"/"odd" 列表。"""
    numbers = case["numbers"]

    # TODO: 遍历 numbers，用 n % 2 判断奇偶
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"numbers": [1, 2, 3, 4]}, ["odd", "even", "odd", "even"]),
        ({"numbers": [10, 7]}, ["even", "odd"]),
        ({"numbers": []}, []),
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

#!/usr/bin/env python3
"""02 · 矩形计算

实现 solve(case)，返回矩形的 [面积, 周长]。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list[int]:
    """返回矩形的 [面积, 周长]。"""
    width = case["width"]
    height = case["height"]

    # TODO: 计算面积和周长
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"width": 3, "height": 4}, [12, 14]),
        ({"width": 5, "height": 2}, [10, 14]),
        ({"width": 0, "height": 5}, [0, 10]),
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

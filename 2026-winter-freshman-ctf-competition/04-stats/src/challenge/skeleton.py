#!/usr/bin/env python3
"""04 · 列表统计

实现 solve(case)，返回 [总和, 最大值, 最小值, 去重升序列表]。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list:
    """返回 [总和, 最大值, 最小值, 去重升序列表]。"""
    numbers = case["numbers"]

    # TODO: 计算总和、最大值、最小值，再去重排序
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"numbers": [3, 1, 7]}, [11, 7, 1, [1, 3, 7]]),
        ({"numbers": [2, 2, 2]}, [6, 2, 2, [2]]),
        ({"numbers": [-5, 0, 5, 0]}, [0, 5, -5, [-5, 0, 5]]),
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

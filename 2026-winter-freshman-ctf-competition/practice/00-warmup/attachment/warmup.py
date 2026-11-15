#!/usr/bin/env python3
"""00 · 热身题：两数相加

实现 solve(case)，返回 a + b。
本地自测：python warmup.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> int:
    """返回 case["a"] + case["b"]。"""
    a = case["a"]
    b = case["b"]

    # TODO: 返回 a 与 b 的和
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"a": 3, "b": 5}, 8),
        ({"a": 0, "b": 0}, 0),
        ({"a": -4, "b": 9}, 5),
        ({"a": 100, "b": -100}, 0),
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

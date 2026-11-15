#!/usr/bin/env python3
"""07 · 单词排行

实现 solve(case)，返回出现次数最多的前 k 个单词。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list[str]:
    """返回出现次数最多的前 k 个单词。"""
    words = case["words"]
    k = case["k"]

    # TODO: 用字典统计次数，再按 (-次数, 单词) 排序
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"words": ["apple", "banana", "apple"], "k": 2}, ["apple", "banana"]),
        ({"words": ["b", "a", "b", "a", "c"], "k": 2}, ["a", "b"]),
        ({"words": ["x"], "k": 3}, ["x"]),
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

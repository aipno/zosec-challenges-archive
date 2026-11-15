#!/usr/bin/env python3
"""05 · 元音统计

实现 solve(case)，统计文本中的元音。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> list:
    """返回 [元音总数, 出现次数最多的元音]。"""
    text = case["text"]

    # TODO: 转小写、统计五个元音的次数，再处理并列
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"text": "Hello World"}, [3, "o"]),
        ({"text": "aeiou AEIOU"}, [10, "a"]),
        ({"text": "xyz"}, [0, ""]),
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

#!/usr/bin/env python3
"""06 · 反转单词

实现 solve(case)，反转句子中的单词顺序。
本地自测：python solution.py
"""

from __future__ import annotations

import sys


def solve(case: dict) -> str:
    """返回反转单词顺序、只留单空格的句子。"""
    sentence = case["sentence"]

    # TODO: 用不带参数的 split() 和 join() 处理空格
    raise NotImplementedError("solve() 还没有实现")


def _self_test() -> int:
    samples = [
        ({"sentence": "hello world"}, "world hello"),
        ({"sentence": "  python   is  fun  "}, "fun is python"),
        ({"sentence": "   "}, ""),
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

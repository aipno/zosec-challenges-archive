# 05 · 元音统计 — Writeup

## 思路

先把文本转小写，只统计 `a/e/i/o/u`。总数是所有元音计数之和；出现次数最多的元音在并列时取字母序最小的。

```python
_VOWELS = "aeiou"

def solve(case: dict) -> list:
    counts = {v: 0 for v in _VOWELS}
    for ch in case["text"].lower():
        if ch in counts:
            counts[ch] += 1
    total = sum(counts.values())
    if total == 0:
        return [0, ""]
    top = min((v for v in _VOWELS if counts[v]), key=lambda v: (-counts[v], v))
    return [total, top]
```

这里用 `min(..., key=(-count, letter))` 同时表达“次数降序、字母升序”。也可以先取最大次数，再在达到最大次数的元音里取最小字母。

边界：`""`、`"xyz"` 返回 `[0, ""]`；`"aeiou AEIOU"` 返回 `[10, "a"]`。

## Flag

`flag{05_7693ba6c8e2d8fc1d80f477791fc62e6}`

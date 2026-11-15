# 06 · 反转单词 — Writeup

## 思路

`s.split()` 不带参数时会按任意空白切分，并自动去掉首尾空白；`" ".join(...)` 再用单空格连接。

```python
def solve(case: dict) -> str:
    return " ".join(reversed(case["sentence"].split()))
```

不要用 `split(" ")`：连续两个空格会产生空字符串，结果里就会多出空格。边界 `"   "` 和 `""` 都返回 `""`。

## Flag

`flag{06_77c930fdcaa77ca43f218dac4e5b1223}`

# 03 · 奇偶名单 — Writeup

## 思路

逐项取模判断。0 是偶数；空列表返回空列表。

```python
def solve(case: dict) -> list[str]:
    return ["even" if n % 2 == 0 else "odd" for n in case["numbers"]]
```

checker 固定包含 `[0]`、`[]`、全偶、全奇，再随机生成 0–20 个 `0..100` 的整数。返回列表长度必须和输入一致。

## Flag

`flag{03_8b6c46aaac79276f68d0399ce9cd0575}`

# 02 · 矩形计算 — Writeup

## 思路

面积是 `width * height`，周长是 `2 * (width + height)`，按 `[面积, 周长]` 返回。

```python
def solve(case: dict) -> list[int]:
    w, h = case["width"], case["height"]
    return [w * h, 2 * (w + h)]
```

边界：宽或高为 0 时面积为 0，周长仍然按公式计算（例如 `0 x 5 -> [0, 10]`）。checker 的 20 组用例里包含 `(0, 5)`、`(1, 1)` 和随机 `0..100`。

## Flag

`flag{02_8da073399fe9a43c4138c34e7979c0eb}`

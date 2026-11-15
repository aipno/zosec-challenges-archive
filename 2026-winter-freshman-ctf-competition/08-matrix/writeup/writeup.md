# 08 · 螺旋矩阵 — Writeup

## 思路

维护四条边界 `top/bottom/left/right`，按“左→右、上→下、右→左、下→上”走一圈，然后收缩边界。关键是走完上边和右边后要判断 `top <= bottom`、`left <= right`，否则最后只剩一行或一列时会重复读取。

```python
def solve(case: dict) -> list[int]:
    matrix = case["matrix"]
    if not matrix:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    order = []
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            order.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            order.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                order.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                order.append(matrix[row][left])
            left += 1
    return order
```

checker 固定包含 `1x1`、`1xN`、`Nx1`、`2x2`、`2x3`，再随机生成 1–6 行、1–6 列的非方阵。

## Flag

`flag{08_8a4254ecadcb0131682c2486430b1211}`

# 04 · 列表统计 — Writeup

## 思路

`sum`、`max`、`min` 直接聚合；去重升序用 `sorted(set(numbers))`。

```python
def solve(case: dict) -> list:
    numbers = case["numbers"]
    return [sum(numbers), max(numbers), min(numbers), sorted(set(numbers))]
```

`numbers` 保证非空，所以不用处理 `max([])`。注意返回顺序是“总和、最大值、最小值、去重列表”，不是排序后的四个数。

## Flag

`flag{04_1ec0d7693ef523e98bc5f7486bba7bb2}`

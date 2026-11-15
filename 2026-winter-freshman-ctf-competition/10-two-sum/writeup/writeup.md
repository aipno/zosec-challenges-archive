# 10 · 两数之和 — Writeup

## 思路

不能写两层循环：大数据用例有 8000–10000 个数，`O(n²)` 会超时。用字典记录“已经见过的数 → 下标”，一次遍历即可。

```python
def solve(case: dict) -> list[int] | None:
    numbers = case["numbers"]
    target = case["target"]
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        if number not in seen:
            seen[number] = index
    return None
```

返回的下标天然满足 `i < j`；`number not in seen` 保证重复数字记录的是第一次出现的位置。checker 只要求任意一对合法下标，不要求特定的一对。

## Flag

`flag{10_4dddd9c16c01b09bea397b239035ab9c}`

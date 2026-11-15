# 07 · 单词排行 — Writeup

## 思路

先用字典统计词频，再按“次数降序、单词字母升序”排序，最后取前 `k` 个。

```python
def solve(case: dict) -> list[str]:
    counts: dict[str, int] = {}
    for word in case["words"]:
        counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts, key=lambda word: (-counts[word], word))
    return ranked[: case["k"]]
```

`k` 大于去重后的单词数时，切片会自动返回全部，不需要额外判断。注意排序后返回的是单词列表，不是 `(单词, 次数)` 对。

## Flag

`flag{07_a37aa144875b1e6231201d19550d406d}`

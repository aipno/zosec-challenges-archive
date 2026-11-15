# 00 · 热身题：两数相加 — Writeup

## 思路

题目要求实现 `solve(case)`，返回 `case["a"] + case["b"]`。

```python
def solve(case: dict) -> int:
    return case["a"] + case["b"]
```

## 验证

把代码填进 `attachment/warmup.py` 的 `solve()`，运行：

```bash
python3 warmup.py
```

4 个样例全部通过后，把整个文件上传即可。`src/challenge/checker.py` 会随机生成 12 组 `-100..100` 的整数，并用 `type(got) is int` 检查返回值类型。

## Flag

`flag{00_cb08178a2a31a14e15926746135fe2b0}`

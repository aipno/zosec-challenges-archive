# 01 · 你好，CTF — Writeup

## 思路

按题面拼接字符串即可。注意标点和空格：`Hello, <name>!`。

```python
def solve(case: dict) -> str:
    return f"Hello, {case['name']}!"
```

也可以写成 `"Hello, " + case["name"] + "!"`，但 f-string 更直接。

`src/challenge/checker.py` 用 10 个固定名字加 10 个随机字母串，共 20 组用例；`compare()` 要求返回值是 `str` 且完全相等。

## 验证

```python
assert solve({"name": "Alice"}) == "Hello, Alice!"
assert solve({"name": "Bob"}) == "Hello, Bob!"
```

## Flag

`flag{01_6a0ceb6cbd13701b1468dd771078c5ca}`

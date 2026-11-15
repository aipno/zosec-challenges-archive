# 09 · 括号校验 — Writeup

## 思路

用列表当栈：遇到左括号入栈并更新最大深度；遇到右括号时检查栈顶是否是对应的左括号。扫描结束后栈必须为空。

```python
_OPEN = "([{"
_MATCH = {")": "(", "]": "[", "}": "{"}

def solve(case: dict) -> list:
    stack = []
    depth = 0
    for ch in case["text"]:
        if ch in _OPEN:
            stack.append(ch)
            depth = max(depth, len(stack))
        elif not stack or stack[-1] != _MATCH[ch]:
            return [False, 0]
        else:
            stack.pop()
    if stack:
        return [False, 0]
    return [True, depth]
```

注意 `"([)]"` 这种“数量对但顺序不对”的情况也要判错；不合法时深度固定返回 0。空串合法，深度为 0。

## Flag

`flag{09_53ba94112820350b03659c87c9a81a56}`

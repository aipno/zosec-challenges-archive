"""Reference solution for 09-brackets."""

from __future__ import annotations

_OPEN = "([{"
_MATCH = {")": "(", "]": "[", "}": "{"}


def solve(case: dict) -> list:
    stack: list[str] = []
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

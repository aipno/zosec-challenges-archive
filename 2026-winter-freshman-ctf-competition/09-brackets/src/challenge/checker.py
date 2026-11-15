"""Checker for 09-brackets."""

from __future__ import annotations

import random

_OPEN = "([{"
_CLOSE = ")]}"
_TWINS = {"(": ")", "[": "]", "{": "}"}
_MATCH = {")": "(", "]": "[", "}": "{"}


def _check(text: str) -> list:
    stack: list[str] = []
    depth = 0
    for ch in text:
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


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = ["", "()", "([])", "{[()]}", "([)]", "(]", "(", ")", "((()))", "{{{}}}"]
    cases = [{"text": text} for text in fixed]
    while len(cases) < count:
        if rng.random() < 0.5:
            stack: list[str] = []
            chunks: list[str] = []
            for _ in range(rng.randint(0, 10)):
                if stack and (rng.random() < 0.55 or len(stack) >= 12):
                    chunks.append(_TWINS[stack.pop()])
                else:
                    opener = rng.choice(_OPEN)
                    stack.append(opener)
                    chunks.append(opener)
            while stack:
                chunks.append(_TWINS[stack.pop()])
            text = "".join(chunks)
        else:
            text = "".join(rng.choice("()[]{}") for _ in range(rng.randint(0, 30)))
        cases.append({"text": text})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> list:
    return _check(case["text"])


def compare(want: list, got: object) -> bool:
    return (
        isinstance(got, list)
        and len(got) == 2
        and type(got[0]) is bool
        and type(got[1]) is int
        and got == want
    )

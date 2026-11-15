"""Checker for 10-two-sum."""

from __future__ import annotations

import random


def generate(rng: random.Random, count: int) -> list[dict]:
    fixed = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([1, 2, 3], 10),
        ([1, 1], 2),
        ([5, 1, 5], 10),
        ([4, 4], 8),
    ]
    cases = [{"numbers": list(numbers), "target": target} for numbers, target in fixed]
    while len(cases) < count:
        size = rng.randint(8000, 10000)
        # Every number except the pair is a multiple of ``modulus``, and the
        # target is not, so only the inserted pair can sum to it.  The pair is
        # inserted at random positions and the list is shuffled: a nested loop
        # still scans the whole list, while "return the last two indices" no
        # longer works.
        modulus = rng.choice((3, 5, 7, 11))
        pair_value = rng.randint(1, modulus // 2)
        target = rng.randrange(-1000000, 1000000) // modulus * modulus + 2 * pair_value
        numbers = [rng.randrange(-500000, 500000) * modulus for _ in range(size)]
        first = rng.randrange(size)
        second = rng.randrange(size - 1)
        if second >= first:
            second += 1
        numbers[first] = pair_value
        numbers[second] = target - pair_value
        rng.shuffle(numbers)
        cases.append({"numbers": numbers, "target": target})
    rng.shuffle(cases)
    return cases[:count]


def expected(case: dict) -> dict:
    numbers = tuple(int(n) for n in case["numbers"])
    target = int(case["target"])
    seen: set[int] = set()
    possible = False
    for number in numbers:
        if target - number in seen:
            possible = True
            break
        seen.add(number)
    return {"possible": possible, "numbers": numbers, "target": target}


def compare(want: dict, got: object) -> bool:
    if not want["possible"]:
        return got is None
    if not isinstance(got, list) or len(got) != 2:
        return False
    i, j = got
    if type(i) is not int or type(j) is not int:
        return False
    if not 0 <= i < j < len(want["numbers"]):
        return False
    return want["numbers"][i] + want["numbers"][j] == want["target"]

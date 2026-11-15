"""Private scene generator for 11-bandit-lite.

Five small levels, each one teaching a different command-line skill:

    level1  hidden file (ls -la)
    level2  permission denied -> chmod
    level3  symlink -> readlink -f
    level4  base64 -> base64 -d
    level5  filename with a space -> quoting

The final token is split into three parts and never appears in one file:

    part1  in level1/.hint (hidden file)
    part2  in level2/secret (mode 000 until chmod)
    part3  in level4/.cipher (base64)

level5 only contains the concatenation rule, so ``grep token`` or
``cat level5/*`` no longer yields the answer.  The broker keeps the complete
expected token in memory.
"""

from __future__ import annotations

import base64
import os
import secrets
from pathlib import Path


def prepare(root: Path, rng, session_id: str, ports: dict) -> dict:
    token = secrets.token_hex(16)
    part1, part2, part3 = token[:11], token[11:22], token[22:]

    level1 = root / "level1"
    level2 = root / "level2"
    level3 = root / "level3"
    level4 = root / "level4"
    level5 = root / "level5"
    for path in (level1, level2, level3, level4, level5):
        path.mkdir(mode=0o755)

    (root / "TASK.md").write_text(
        "# Bandit-lite\n"
        "\n"
        "5 个关卡。最终 token 被拆成 part1、part2、part3，分别藏在前几关，\n"
        "level5 里写着拼接顺序。\n"
        "从 level1 开始，每一关的线索会告诉你下一步。\n"
        "最后把拼出来的 32 位十六进制 token 提交到网页。\n",
        encoding="utf-8",
    )

    (level1 / "README").write_text(
        "第 1 关\n"
        "======\n"
        "这一层放着一份交接记录，但它没有出现在普通列目录的结果里。\n",
        encoding="utf-8",
    )
    (level1 / ".hint").write_text(
        "第 1 关通过。\n"
        f"part1={part1}\n"
        "下一关：level2/secret。它现在谁也不让读。\n",
        encoding="utf-8",
    )

    secret = level2 / "secret"
    secret.write_text(
        "第 2 关通过。\n"
        f"part2={part2}\n"
        "下一关：level3/link。它不是它看起来的样子。\n",
        encoding="utf-8",
    )
    os.chmod(secret, 0o000)
    (level2 / "decoy.txt").write_text("这不是下一关，别被骗了。\n", encoding="utf-8")

    (level3 / "link").symlink_to("../level4/.cipher")

    clue = (
        "第 3 关通过。\n"
        f"part3={part3}\n"
        "下一关：level5/with space.txt。先去读它，再按里面的规则拼接三部分。\n"
    )
    (level4 / ".cipher").write_text(
        base64.b64encode(clue.encode("utf-8")).decode("ascii") + "\n",
        encoding="utf-8",
    )

    final = level5 / "with space.txt"
    final.write_text(
        "第 5 关到了。\n"
        "token = part1 + part2 + part3\n"
        "把前面三关拿到的片段按这个顺序拼起来，就是 32 位 token。\n",
        encoding="utf-8",
    )
    (level5 / "decoy.txt").write_text("这里没有 token。\n", encoding="utf-8")

    return {
        "answer": token,
        "banner": (
            "=== Bandit-lite ===\r\n"
            "5 个关卡，token 由 part1、part2、part3 拼接而成。\r\n"
            "从 level1/README 开始。\r\n"
            "\r\n"
        ),
    }

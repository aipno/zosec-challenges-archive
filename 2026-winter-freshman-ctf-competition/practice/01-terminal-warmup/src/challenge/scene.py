"""Private scene generator for 01-terminal-warmup.

A deliberately tiny first terminal task: one hidden file and one visible
README.  The token is random for every session and only the broker knows the
expected value.
"""

from __future__ import annotations

import secrets
from pathlib import Path


def prepare(root: Path, rng, session_id: str, ports: dict) -> dict:
    token = secrets.token_hex(16)

    (root / "README.txt").write_text(
        "欢迎来到终端热身题。\n"
        "\n"
        "1. 执行 ls -la，找到以 . 开头的隐藏文件。\n"
        "2. 用 cat 打开 .welcome。\n"
        "3. 把 token=... 的值提交到网页。\n"
        "\n"
        "如果终端没有反应，先点一下终端区域再输入。\n",
        encoding="utf-8",
    )
    (root / ".welcome").write_text(
        "恭喜，你找到了隐藏文件。\n"
        f"token={token}\n"
        "\n"
        "把 token 的值填到网页的输入框里，领取 flag。\n",
        encoding="utf-8",
    )

    return {
        "answer": token,
        "banner": (
            "=== 终端热身 ===\r\n"
            "这是一台隔离的 Linux 沙箱。先试试 ls -la。\r\n"
            "\r\n"
        ),
    }

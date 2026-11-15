"""Private scene generator for 12-proc-hunt.

The broker starts three long-running ``sleep`` processes as the session's own uid.  Each
one holds an unlinked file descriptor open; exactly one of those files
contains the real token.  The player must inspect ``ps`` and ``/proc/<pid>/fd``
to find it.  The expected token lives only in the broker's memory.
"""

from __future__ import annotations

import secrets
from pathlib import Path


def prepare(root: Path, rng, session_id: str, ports: dict) -> dict:
    token = secrets.token_hex(16)
    names = ["backup-agent", "sync-worker", "log-shipper"]
    rng.shuffle(names)

    (root / "README.md").write_text(
        "# 进程猎手\n"
        "\n"
        "这个沙箱里有三个长期运行的后台进程。\n"
        "其中一个进程手里还拿着一个已经从目录里删掉、但还没有真正离开系统的文件，\n"
        "文件里有一行 token=...。另外两个是诱饵。\n"
        "\n"
        "注意：不要杀掉进程。进程一退出，线索就没了。\n"
        "\n"
        "找到 token 后，把值提交到网页。\n",
        encoding="utf-8",
    )

    victims = [
        {"name": names[0], "token": token, "sleep": 3600},
        {"name": names[1], "decoy": "not the token (decoy 1)", "sleep": 3600},
        {"name": names[2], "decoy": "not the token (decoy 2)", "sleep": 3600},
    ]

    return {
        "answer": token,
        "victims": victims,
        "banner": (
            "=== 进程猎手 ===\r\n"
            "三个后台进程，其中一个还攼着 token。\r\n"
            "先看看 README.md。\r\n"
            "\r\n"
        ),
    }

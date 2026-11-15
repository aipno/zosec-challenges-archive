"""Private scene generator for 13-fix-server.

The scene contains a broken static site:

  * server/run.sh is not executable
  * server/config.ini points at the wrong host/port/root
  * site/health.txt is mode 000

The broker runs a loopback gate on ``ports["gate"]`` as root.  The gate holds
the token in memory and only returns it after:

  * server/run.sh is executable
  * server/config.ini matches the expected host/port/root
  * site/health.txt is owner-readable and contains the marker
  * the player's server on ``ports["site"]`` serves /health.txt with marker
    and an ``X-Health-Marker`` header (the provided site_server.py does this;
    a bare ``python3 -m http.server`` does not)

The player can fix all of those files, but cannot read the token from disk.
"""

from __future__ import annotations

import os
import secrets
from pathlib import Path


def prepare(root: Path, rng, session_id: str, ports: dict) -> dict:
    token = secrets.token_hex(16)
    marker = "health-" + secrets.token_hex(12)
    gate_port = int(ports["gate"])
    site_port = int(ports["site"])
    site_root = root / "site"

    server = root / "server"
    site = site_root
    assets = site / "assets"
    for path in (server, site, assets):
        path.mkdir(mode=0o755, parents=True)

    (root / "TASK.md").write_text(
        "# 修好这个站点\n"
        "\n"
        "本次会话的参数：\n"
        "\n"
        f"    SITE_PORT={site_port}\n"
        f"    SITE_ROOT={site_root}\n"
        f"    GATE_PORT={gate_port}\n"
        "\n"
        "站点在 `server/` 下，静态文件在 `site/` 下，现在起不来。\n"
        "\n"
        "修好之后让它在后台运行，然后访问健康检查服务领取 token：\n"
        "\n"
        f"       http://127.0.0.1:{gate_port}/token\n"
        "\n"
        "返回 `{\"ok\": true, \"token\": \"...\"}` 后，把 token 提交到网页。\n"
        "返回 403 时读 `checks` 字段，它会逐项告诉你还差哪一项。\n"
        "\n"
        "参数也写在 `.task-env` 里，可以 `source .task-env` 后使用 $SITE_PORT 等变量。\n",
        encoding="utf-8",
    )
    (root / ".task-env").write_text(
        f"SITE_PORT={site_port}\n"
        f"SITE_ROOT={site_root}\n"
        f"GATE_PORT={gate_port}\n",
        encoding="utf-8",
    )

    (server / "config.ini").write_text(
        "[server]\n"
        "host = 0.0.0.0\n"
        "port = 1\n"
        "root = ../site\n",
        encoding="utf-8",
    )
    (server / "run.sh").write_text(
        "#!/bin/sh\n"
        "set -eu\n"
        "cd \"$(dirname \"$0\")\"\n"
        "exec python3 site_server.py --config config.ini\n",
        encoding="utf-8",
    )
    (server / "site_server.py").write_text(
        "#!/usr/bin/env python3\n"
        "import argparse\n"
        "import configparser\n"
        "import functools\n"
        "import http.server\n"
        "import os\n"
        "\n"
        "\n"
        "def main() -> None:\n"
        "    parser = argparse.ArgumentParser()\n"
        "    parser.add_argument(\"--config\", required=True)\n"
        "    args = parser.parse_args()\n"
        "\n"
        "    config = configparser.ConfigParser(interpolation=None)\n"
        "    config.read(args.config, encoding=\"utf-8\")\n"
        "    section = config[\"server\"]\n"
        "    host = section[\"host\"].strip()\n"
        "    port = int(section[\"port\"].strip())\n"
        "    root = os.path.abspath(section[\"root\"].strip())\n"
        "\n"
        "    marker = open(os.path.join(root, \"health.txt\"), encoding=\"utf-8\").read().strip()\n"
        "\n"
        "    class Handler(http.server.SimpleHTTPRequestHandler):\n"
        "        def end_headers(self):\n"
        "            if self.path.split(\"?\", 1)[0] == \"/health.txt\":\n"
        "                self.send_header(\"X-Health-Marker\", marker)\n"
        "            super().end_headers()\n"
        "\n"
        "    handler = functools.partial(Handler, directory=root)\n"
        "    http.server.ThreadingHTTPServer((host, port), handler).serve_forever()\n"
        "\n"
        "\n"
        "if __name__ == \"__main__\":\n"
        "    main()\n",
        encoding="utf-8",
    )

    (site / "index.html").write_text(
        "<!doctype html>\n"
        "<html lang=\"zh-CN\"><head><meta charset=\"utf-8\">\n"
        "<title>修复站点</title>\n"
        "<link rel=\"stylesheet\" href=\"assets/style.css\">\n"
        "</head><body><h1>站点已启动</h1>\n"
        "<p>接下来去访问健康检查服务领取 token。</p>\n"
        "</body></html>\n",
        encoding="utf-8",
    )
    (assets / "style.css").write_text(
        "body { font-family: system-ui, sans-serif; margin: 3rem; }\n"
        "h1 { color: #3457d5; }\n",
        encoding="utf-8",
    )
    (site / "health.txt").write_text(marker + "\n", encoding="utf-8")

    # Deliberate breakage: the site server runs as the sandbox user, and
    # these two files are not usable in the initial state.
    os.chmod(server / "run.sh", 0o644)
    os.chmod(site / "health.txt", 0o000)

    return {
        "answer": token,
        "gate": {
            "port": gate_port,
            "token": token,
            "marker": marker,
            "upstream_port": site_port,
            "expected": {
                "host": "127.0.0.1",
                "port": site_port,
                "root": str(site_root),
            },
            "config_path": "server/config.ini",
            "run_path": "server/run.sh",
            "health_path": "site/health.txt",
        },
        "banner": (
            "=== 修好这个站点 ===\r\n"
            "先 cat TASK.md。\r\n"
            "修好后访问健康检查端口领 token。\r\n"
            "\r\n"
        ),
    }

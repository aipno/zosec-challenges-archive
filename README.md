# CTF 题目归档

本目录收录比赛结束后的公开复盘材料。

## 比赛

- [2026 冬季新生 CTF 挑战赛](2026-winter-freshman-ctf-competition/)：23 道计分题 + 2 道赛前热身题，总分 10000。

## 每题保留什么

```text
<比赛>/<题目>/
├── README.md          # 标题、作者、方向、知识点、难度、题面、提示、flag
├── attachment/        # 比赛时发给选手的附件（没有附件时不存在）
├── src/               # 题目源码（checker/scene/content/app）
├── env/               # 容器题：本地 docker pull/run 命令（镜像可匿名拉取）
└── writeup/
    └── writeup.md     # 赛后题解
```

- `README.md` 采用与参考仓库一致的字段：标题、作者、方向、知识点、难度、内容、提示、是否可共享、备注、FLAG。
- `attachment/` 只放选手实际拿到的文件；动态附件题保留 1 份样例，完整 flag 列表在该题目录的 `flags.txt`。
- `src/` 只放题目本身的源码，例如 Python 题的 `checker.py`、终端题的 `scene.py`、Web 题的 `app.py`。
- `env/` 只给容器题：`README.md` 是本地 `docker pull` + `docker run` 命令，镜像托管在 `docker.iswxl.cn`，允许匿名拉取；动态附件题没有 `env/`。
- `writeup/` 是赛后整理的题解，包含思路、关键代码/命令和 flag。

## 本地镜像复盘

21 道容器题在各自目录的 `env/README.md` 提供本地运行命令，镜像托管在 `docker.iswxl.cn`，tag 为 `:archive`，允许匿名拉取，不需要登录。按题目目录的 `env/README.md` 拉取和运行。例如：

```bash
docker pull docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive
docker run --rm -p 8081:8000 -e HOME=/tmp \
  -e 'FLAG=flag{01_6a0ceb6cbd13701b1468dd771078c5ca}' \
  docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive
# 打开 http://127.0.0.1:8081
```

完整镜像列表、端口和每题命令见 [`2026-winter-freshman-ctf-competition/env/README.md`](2026-winter-freshman-ctf-competition/env/README.md)。

## 没有收录什么

为保持公开归档干净、可读，以下开发文件**不在**本目录中：

- 平台前端（`web/`）、Python judge、终端 broker、Web 共享运行时 `common/`；
- `Dockerfile`、`docker-compose*.yml`、`Makefile`、`entrypoint.sh`、`scripts/`、`tests/`；
- `__pycache__`、`.pyc`、本地开发 flag 配置、原始压缩包、出题文档和评分表。

因此本目录**不是从源码一键构建的部署包**：不提供 Dockerfile/compose；容器题镜像托管在 `docker.iswxl.cn`（匿名可拉取），仓库里只保留 `env/README.md` 运行说明。动态附件题仍按题解直接分析附件。

## Flag 说明

- 容器题（Python、终端、Web）在比赛中由平台给每个实例注入动态 flag；README 里给出的是本地复现用 flag。
- 动态附件题（14/15/16/18）每道有 50 个 flag，`attachment/` 里是 1 份样例，完整列表在各题目录的 `flags.txt`。
- 容器题镜像在 `docker.iswxl.cn`（tag `:archive`），允许匿名拉取，只有推送需要管理员登录；本仓库不保存镜像 tar。
- 所有 flag 仅用于赛后复盘和本地验证。

## 许可

MIT，见 [`LICENSE`](LICENSE)。

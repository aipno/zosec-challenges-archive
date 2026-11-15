# 2026 冬季新生 CTF 挑战赛

2026 冬季新生 CTF 挑战赛的赛后归档。比赛为线上个人 Jeopardy 赛，时间 2026-11-15 18:00–20:20（UTC+8），共 23 道计分题、总分 10000 分；另有 2 道赛前热身题，不计入成绩。

本目录按题目拆分，每题保留题目源码、选手附件、题解和 flag，方便赛后复盘。运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

## 计分题

| # | 题目 | 分类 | 难度 | 分值 | 目录 |
|---|---|---|---|---|---|
| 01 | [你好，CTF](01-hello/) | Python | 1/10 | 200 | `01-hello/` |
| 02 | [矩形计算](02-rect/) | Python | 2/10 | 260 | `02-rect/` |
| 03 | [奇偶名单](03-even/) | Python | 3/10 | 360 | `03-even/` |
| 04 | [列表统计](04-stats/) | Python | 4/10 | 400 | `04-stats/` |
| 05 | [元音统计](05-vowels/) | Python | 5/10 | 460 | `05-vowels/` |
| 06 | [反转单词](06-reverse-words/) | Python | 6/10 | 540 | `06-reverse-words/` |
| 07 | [单词排行](07-count-words/) | Python | 7/10 | 620 | `07-count-words/` |
| 08 | [螺旋矩阵](08-matrix/) | Python | 8/10 | 760 | `08-matrix/` |
| 09 | [括号校验](09-brackets/) | Python | 9/10 | 900 | `09-brackets/` |
| 10 | [两数之和](10-two-sum/) | Python | 10/10 | 1000 | `10-two-sum/` |
| 11 | [Bandit-lite：五关小迷宫](11-bandit-lite/) | 终端 | 5/10 | 500 | `11-bandit-lite/` |
| 12 | [进程猎手](12-proc-hunt/) | 终端 | 6/10 | 580 | `12-proc-hunt/` |
| 13 | [修好这个站点](13-fix-server/) | 终端 | 7/10 | 660 | `13-fix-server/` |
| 14 | [一张奇怪的纸条](14-misc-base64/) | Misc | 1/10 | 200 | `14-misc-base64/` |
| 15 | [罗马将军的笔记](15-crypto-rot13/) | Crypto | 1/10 | 200 | `15-crypto-rot13/` |
| 16 | [被 XOR 过的秘密](16-crypto-xor/) | Crypto | 2/10 | 300 | `16-crypto-xor/` |
| 17 | [登录页面](17-web-view-source/) | Web | 1/10 | 200 | `17-web-view-source/` |
| 18 | [打不开的图片](18-misc-fake-png/) | Misc | 2/10 | 260 | `18-misc-fake-png/` |
| 19 | [运维小站](19-web-robots/) | Web | 1/10 | 240 | `19-web-robots/` |
| 20 | [MiniShop 商城](20-web-git-leak/) | Web | 2/10 | 320 | `20-web-git-leak/` |
| 21 | [管理后台登录](21-web-brute-login/) | Web | 2/10 | 320 | `21-web-brute-login/` |
| 22 | [支付密码](22-web-brute-pin/) | Web | 2/10 | 360 | `22-web-brute-pin/` |
| 23 | [会员登录](23-web-sqli/) | Web | 2/10 | 360 | `23-web-sqli/` |

## 赛前热身（不计分）

| # | 题目 | 类型 | 难度 | 分值 | 目录 |
|---|---|---|---|---|---|
| 00 | [热身题：两数相加](practice/00-warmup/) | Python | 1/10 | — | `practice/00-warmup/` |
| 01 | [终端热身：隐藏文件里的 token](practice/01-terminal-warmup/) | 终端 | 1/10 | — | `practice/01-terminal-warmup/` |

## 分类小计

| 分类 | 题号 | 题数 | 分值 |
|---|---|---|---|
| Python | 01–10 | 10 | 5500 |
| 终端 | 11–13 | 3 | 1740 |
| Misc | 14、18 | 2 | 460 |
| Crypto | 15、16 | 2 | 500 |
| Web | 17、19–23 | 6 | 1800 |
| **合计** | 01–23 | **23** | **10000** |

## 目录约定

每道题一个目录：

```text
<题目>/
├── README.md          # 标题、作者、方向、知识点、难度、题面、提示、flag
├── attachment/        # 发给选手的附件（没有附件时不存在）
├── src/               # 题目源码（meta + checker/scene/content/app）
├── env/               # 容器题：本地 docker pull/run 命令（镜像可匿名拉取）
└── writeup/
    └── writeup.md     # 赛后题解
```

- Python 题：`attachment/` 是选手下载的骨架；`src/challenge/` 含 checker 和 reference。
- 终端题：没有附件；`src/challenge/scene.py` 是场景生成器。
- 动态附件题：`attachment/` 保留 1 份样例，`flags.txt` 是完整 50 个 flag。
- Web 题：`src/app/`（19–23）或 `src/challenge/content.py`（17）是题目源码。
- 容器题：`env/README.md` 是本地 `docker pull` + `docker run` 命令，镜像托管在 `docker.iswxl.cn`，允许匿名拉取；动态附件题没有 `env/`。

## 本地镜像复盘

21 道容器题（01–13、17、19–23、practice）的镜像托管在 `docker.iswxl.cn`，tag 为 `:archive`，允许匿名拉取，不需要登录；14/15/16/18 是动态附件题，没有镜像。

按题目目录的 `env/README.md` 拉取和运行。例如：

```bash
docker pull docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive
docker run --rm -p 8081:8000 -e HOME=/tmp \
  -e 'FLAG=flag{01_6a0ceb6cbd13701b1468dd771078c5ca}' \
  docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive
```

完整镜像列表、端口和本地 flag 见 [`env/README.md`](env/README.md) 和各题目录的 `env/README.md`。

## 说明

- 容器题在比赛中使用平台按实例注入的动态 flag；README 中列出的是本地复现用 flag。
- 动态附件题有 50 个 flag；样例附件对应其中一个，完整列表见各题目录的 `flags.txt`。
- 所有 flag 仅用于复盘和本地验证，比赛结束后已不再有效。
- 容器题镜像托管在 `docker.iswxl.cn`（tag `:archive`），允许匿名拉取，只有推送需要管理员登录；本仓库不保存镜像 tar。
- 本题库以 MIT 许可发布，见 [`LICENSE`](../LICENSE)。

# 本地镜像复盘

21 道容器题每题提供一个预构建镜像，托管在 `docker.iswxl.cn`，允许匿名拉取，tag 为 `:archive`。
14/15/16/18 是动态附件题，没有镜像，直接使用 `attachment/` 下的文件和 `flags.txt`。

## 拉取与运行

镜像允许匿名拉取，不需要登录：

```bash
docker pull docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive
docker run --rm -p 8081:8000 -e HOME=/tmp \
  -e 'FLAG=flag{01_6a0ceb6cbd13701b1468dd771078c5ca}' \
  docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive
```

然后打开 <http://127.0.0.1:8081>。每道题的完整命令、端口和 flag 见该题目录的 `env/README.md`。

## 镜像列表

| # | 题目 | 本地端口 | 镜像 | 目录 |
|---|---|---|---|---|
| 热身 00 | 热身题：两数相加 | 8099 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/warmup:archive` | [`practice/00-warmup/env/`](../practice/00-warmup/env/) |
| 01 | 你好，CTF | 8081 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive` | [`01-hello/env/`](../01-hello/env/) |
| 02 | 矩形计算 | 8082 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/rect:archive` | [`02-rect/env/`](../02-rect/env/) |
| 03 | 奇偶名单 | 8083 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/even:archive` | [`03-even/env/`](../03-even/env/) |
| 04 | 列表统计 | 8084 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/stats:archive` | [`04-stats/env/`](../04-stats/env/) |
| 05 | 元音统计 | 8085 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/vowels:archive` | [`05-vowels/env/`](../05-vowels/env/) |
| 06 | 反转单词 | 8086 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/reverse-words:archive` | [`06-reverse-words/env/`](../06-reverse-words/env/) |
| 07 | 单词排行 | 8087 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/count-words:archive` | [`07-count-words/env/`](../07-count-words/env/) |
| 08 | 螺旋矩阵 | 8088 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/matrix:archive` | [`08-matrix/env/`](../08-matrix/env/) |
| 09 | 括号校验 | 8089 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/brackets:archive` | [`09-brackets/env/`](../09-brackets/env/) |
| 10 | 两数之和 | 8090 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/two-sum:archive` | [`10-two-sum/env/`](../10-two-sum/env/) |
| 11 | Bandit-lite：五关小迷宫 | 8101 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/bandit-lite:archive` | [`11-bandit-lite/env/`](../11-bandit-lite/env/) |
| 12 | 进程猎手 | 8102 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/proc-hunt:archive` | [`12-proc-hunt/env/`](../12-proc-hunt/env/) |
| 13 | 修好这个站点 | 8103 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/fix-server:archive` | [`13-fix-server/env/`](../13-fix-server/env/) |
| 17 | 登录页面 | 8124 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-view-source:archive` | [`17-web-view-source/env/`](../17-web-view-source/env/) |
| 19 | 运维小站 | 8126 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-robots:archive` | [`19-web-robots/env/`](../19-web-robots/env/) |
| 20 | MiniShop 商城 | 8127 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-git-leak:archive` | [`20-web-git-leak/env/`](../20-web-git-leak/env/) |
| 21 | 管理后台登录 | 8128 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-brute-login:archive` | [`21-web-brute-login/env/`](../21-web-brute-login/env/) |
| 22 | 支付密码 | 8129 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-brute-pin:archive` | [`22-web-brute-pin/env/`](../22-web-brute-pin/env/) |
| 23 | 会员登录 | 8130 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-sqli:archive` | [`23-web-sqli/env/`](../23-web-sqli/env/) |
| 热身 01 | 终端热身：隐藏文件里的 token | 8098 | `docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/terminal-warmup:archive` | [`practice/01-terminal-warmup/env/`](../practice/01-terminal-warmup/env/) |

## 说明

- 镜像不在本仓库中，存放在 `docker.iswxl.cn`；允许匿名拉取，只有推送镜像需要管理员登录。
- 镜像内不含 flag；运行时通过 `FLAG` 环境变量注入本地复现 flag。
- 比赛时的 flag 由平台按实例动态生成，和这里的本地 flag 不同。
- 需要 Docker 20.10+；镜像架构是 `linux/amd64`，Apple Silicon 上 Docker 会自动模拟，也可以加 `--platform linux/amd64`。
- 所有容器都只暴露容器内 `8000` 端口；按上表映射到本地端口即可。

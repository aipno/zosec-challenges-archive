# 13 · 修好这个站点 — 本地镜像复盘

- 镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/fix-server:archive`
- 容器端口：`8000`
- 本地端口：`8103`
- 本地复现 flag：`flag{13_f2743f76386e24793f64870f}`
- 架构：`linux/amd64`

## 拉取

镜像托管在 `docker.iswxl.cn`。匿名用户可以直接拉取，不需要登录：

```bash
docker pull docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/fix-server:archive
```

## 运行

```bash
docker run --rm \
  -p 8103:8000 \
  -e HOME=/tmp \
  -e 'FLAG=flag{13_f2743f76386e24793f64870f}' \
  docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/fix-server:archive
```

浏览器打开 <http://127.0.0.1:8103>。

按 `Ctrl+C` 停止；`--rm` 会自动清理容器，镜像本身保留，可以重复运行。

## 说明

- 镜像不在本仓库中，存放在 `docker.iswxl.cn`；允许匿名拉取，只有推送镜像需要管理员登录。
- 镜像内不含 flag；`FLAG` 环境变量在启动时注入。
- 比赛时平台给每个实例注入不同的动态 flag；上面是本地复现用 flag。
- 本题是交互式终端。gate 和 site 都在容器内的 127.0.0.1 上，不需要额外映射端口。
- 需要 Docker 20.10+；镜像架构是 `linux/amd64`，Apple Silicon 上 Docker 会自动模拟，也可以加 `--platform linux/amd64`。

题解见 [`../writeup/writeup.md`](../writeup/writeup.md)。

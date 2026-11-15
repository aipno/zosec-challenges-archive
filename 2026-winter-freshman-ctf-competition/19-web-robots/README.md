# 19 · 运维小站

### 作者
aipno

### 方向
Web

### 知识点
robots.txt、HTML 注释泄露

### 难度
简单（1/10）

### 内容
一个运维小站，首页只有几行冷冰冰的公告。

找出站点里隐藏的 flag。

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：单容器 Web 题；比赛分值：240 分。
- 来源：原题来自项目根目录 `web题.zip` → `challenges/c1_info_robots/app.py` 与 `_shared/templates/c1_*.html`，在 `zips/19-web-robots/` 中改为单容器 Web 题。
- 归档：`src/app/` 是题目的 Flask 应用与模板；`src/challenge/meta.json` 是题目元数据。归档不含平台共享的 `common` 运行时，运行环境需自行补齐。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-robots:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{0e7f41bf26743dc8adb81bbe0a0a8328}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

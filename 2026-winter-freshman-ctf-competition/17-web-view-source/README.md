# 17 · 登录页面

### 作者
aipno

### 方向
Web

### 知识点
前端源码、硬编码凭据

### 难度
简单（1/10）

### 内容
一个内部管理系统的登录页。随便输什么都登不进去。

打开题目文件 login.html，找出隐藏的 flag。

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：单容器 Web 题；比赛分值：200 分。
- 来源：原题来自项目根目录 `web题.zip` → `ctf-practice/challenge4-web/login.html`，在 `zips/17-web-view-source/` 中改为容器内生成动态 flag。
- 归档：`attachment/login.html` 是用本地 flag 生成的样例页面；`src/challenge/` 含 `meta.json` 和页面生成器 `content.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-view-source:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{1d665433e9a4b74dfcd6e35f94ea4724}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

# 20 · MiniShop 商城

### 作者
aipno

### 方向
Web

### 知识点
.git 泄露、目录列表、备份文件泄露

### 难度
简单（2/10）

### 内容
MiniShop 商城只剩一个空荡荡的首页：商品列表和购物车的链接都还在，页面本身却没什么内容。

从站点里找出 flag。

### 提示
- 版本控制目录和编辑器备份文件如果留在线上，是可以直接读的。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：单容器 Web 题；比赛分值：320 分。
- 来源：原题来自项目根目录 `web题.zip` → `challenges/c2_info_git/app.py` 与 `_shared/templates/c2_home.html`，在 `zips/20-web-git-leak/` 中改为单容器 Web 题。
- 归档：`src/app/` 是题目的 Flask 应用与模板；`src/challenge/meta.json` 是题目元数据。归档不含平台共享的 `common` 运行时，运行环境需自行补齐。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-git-leak:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{f23fa972baf0a41af89535f5ddbcf41a}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

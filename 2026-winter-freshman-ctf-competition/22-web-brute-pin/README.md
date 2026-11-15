# 22 · 支付密码

### 作者
aipno

### 方向
Web

### 知识点
4 位 PIN 爆破、失败限速处理

### 难度
简单（2/10）

### 内容
支付密码验证页：只有 4 位数字。

猜出 PIN，拿到 flag。

### 提示
- 限速只拦失败的尝试：被限速时重试同一个 PIN，别跳过；页面用 data-result 区分成功、失败和被限速。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：单容器 Web 题；比赛分值：360 分。
- 来源：原题来自项目根目录 `web题.zip` → `challenges/c4_brute_pin/app.py` 与 `_shared/templates/c4_pin.html`，在 `zips/22-web-brute-pin/` 中改为单容器 Web 题。
- 归档：`src/app/` 是题目的 Flask 应用与模板；`src/challenge/meta.json` 是题目元数据。归档不含平台共享的 `common` 运行时，运行环境需自行补齐。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/zips-web-brute-pin:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{997b1d5ae9562c9a7c46899c3ba980fe}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

# 热身 · 01 · 隐藏文件里的 token

### 作者
aipno

### 方向
终端

### 知识点
ls -la、隐藏文件、cat

### 难度
简单（1/10）

### 内容
这是一道赛前热身题，不计入比赛成绩。

网页下方是一台隔离的 Linux 沙箱，直接输入命令即可。

任务：
1. 执行 ls -la，注意以 . 开头的隐藏文件。
2. 用 cat 打开 .welcome。
3. 把文件里的 token=... 填到下方输入框，领取 flag。

提示：Tab 补全、方向键、Ctrl+C 都可以用。
刷新页面会短暂断开连接；同一标签页 30 秒内会自动续上，超时后会话结束。

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：交互式终端（赛前热身）；比赛分值：不计分（赛前热身）。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/practice/01-terminal-warmup/` 的赛前热身题。
- 归档：`src/challenge/` 含 `meta.json` 和场景生成器 `scene.py`；没有选手附件，选手在浏览器终端里操作。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/terminal-warmup:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{01_b56ae2d50665b22c5daeef66}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

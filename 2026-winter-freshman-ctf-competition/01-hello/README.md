# 01 · 你好，CTF

### 作者
aipno

### 方向
Python

### 知识点
变量、字符串、f-string

### 难度
简单（1/10）

### 内容
实现 solve(case)，返回一句问候语。

case 形如 {"name": "Alice"}，返回 "Hello, Alice!"。

示例：
name = "Alice" -&gt; "Hello, Alice!"
name = "Bob" -&gt; "Hello, Bob!"

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：200 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/01-hello/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/hello:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{01_6a0ceb6cbd13701b1468dd771078c5ca}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

# 03 · 奇偶名单

### 作者
aipno

### 方向
Python

### 知识点
for 循环、取模、if/else、空列表

### 难度
简单（3/10）

### 内容
实现 solve(case)，判断 case["numbers"] 中每个整数的奇偶。

偶数返回 "even"，奇数返回 "odd"。0 是偶数，空列表返回空列表。

示例：
[1, 2, 3, 4] -&gt; ["odd", "even", "odd", "even"]
[10, 7] -&gt; ["even", "odd"]
[] -&gt; []

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：360 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/03-even/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/even:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{03_8b6c46aaac79276f68d0399ce9cd0575}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

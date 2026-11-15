# 05 · 元音统计

### 作者
aipno

### 方向
Python

### 知识点
字符串遍历、大小写处理、字典计数、并列取舍

### 难度
中等（5/10）

### 内容
实现 solve(case)，统计 case["text"] 里的元音，返回 [元音总数, 出现次数最多的元音]。

元音只有 a、e、i、o、u，大小写都算，结果里的元音用小写。

- 没有元音时返回 [0, ""]
- 多个元音的次数并列最多时，取字母序最小的那个

示例：
"Hello World" -&gt; [3, "o"]
"aeiou AEIOU" -&gt; [10, "a"]
"xyz" -&gt; [0, ""]

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：460 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/05-vowels/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/vowels:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{05_7693ba6c8e2d8fc1d80f477791fc62e6}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

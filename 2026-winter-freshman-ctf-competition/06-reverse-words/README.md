# 06 · 反转单词

### 作者
aipno

### 方向
Python

### 知识点
split / join、空白处理

### 难度
中等（6/10）

### 内容
实现 solve(case)，把 case["sentence"] 的单词顺序反转后返回。

句子可能有前导、尾随和连续空格。返回时去掉首尾空格，单词之间只用一个空格连接；没有单词时返回 ""。

示例：
"hello world" -&gt; "world hello"
"  python   is  fun  " -&gt; "fun is python"
"   " -&gt; ""

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：540 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/06-reverse-words/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/reverse-words:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{06_77c930fdcaa77ca43f218dac4e5b1223}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

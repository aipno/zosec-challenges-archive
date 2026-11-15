# 07 · 单词排行

### 作者
aipno

### 方向
Python

### 知识点
字典计数、多级排序、切片

### 难度
中等（7/10）

### 内容
实现 solve(case)，统计 case["words"] 中每个单词的出现次数，返回出现最多的前 case["k"] 个单词。

排序规则：

- 次数多的排在前面
- 次数相同时，按单词字母序升序
- 去重后不足 k 个时，返回全部

示例：
{"words": ["apple", "banana", "apple"], "k": 2} -&gt; ["apple", "banana"]
{"words": ["b", "a", "b", "a", "c"], "k": 2} -&gt; ["a", "b"]
{"words": ["x"], "k": 3} -&gt; ["x"]

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：620 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/07-count-words/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/count-words:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{07_a37aa144875b1e6231201d19550d406d}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

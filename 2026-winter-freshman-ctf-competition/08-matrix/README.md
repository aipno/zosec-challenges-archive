# 08 · 螺旋矩阵

### 作者
aipno

### 方向
Python

### 知识点
二维列表遍历、四条边界收缩

### 难度
困难（8/10）

### 内容
实现 solve(case)，把 case["matrix"] 中的数字按螺旋顺序读出来，返回一个列表。

螺旋顺序：从左到右、从上到下、从右到左、从下到上，一圈一圈向里收。

示例：
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] -&gt; [1, 2, 3, 6, 9, 8, 7, 4, 5]
[[1, 2, 3]] -&gt; [1, 2, 3]
[[1], [2], [3]] -&gt; [1, 2, 3]
[[1, 2], [3, 4]] -&gt; [1, 2, 4, 3]

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：760 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/08-matrix/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/matrix:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{08_8a4254ecadcb0131682c2486430b1211}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

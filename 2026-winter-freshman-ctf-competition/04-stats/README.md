# 04 · 列表统计

### 作者
aipno

### 方向
Python

### 知识点
列表聚合、set 去重、排序

### 难度
中等（4/10）

### 内容
实现 solve(case)，对 case["numbers"] 汇总后返回 [总和, 最大值, 最小值, 去重升序列表]。

case["numbers"] 是非空整数列表，可能有重复，也可能有负数。

示例：
[3, 1, 7] -&gt; [11, 7, 1, [1, 3, 7]]
[2, 2, 2] -&gt; [6, 2, 2, [2]]
[-5, 0, 5, 0] -&gt; [0, 5, -5, [-5, 0, 5]]

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：400 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/04-stats/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/stats:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{04_1ec0d7693ef523e98bc5f7486bba7bb2}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

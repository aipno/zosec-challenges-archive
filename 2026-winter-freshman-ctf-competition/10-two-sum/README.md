# 10 · 两数之和

### 作者
aipno

### 方向
Python

### 知识点
哈希表、一次遍历、O(n) 复杂度

### 难度
困难（10/10）

### 内容
实现 solve(case)，在 case["numbers"] 中找两个不同位置 i &lt; j，使 numbers[i] + numbers[j] == target。

- 找到任意一对即可，返回 [i, j]
- 找不到时返回 None
- 大数据用例每组最多约 1 万个数

示例：
numbers = [2, 7, 11, 15], target = 9 -&gt; [0, 1]
numbers = [3, 2, 4], target = 6 -&gt; [1, 2]
numbers = [1, 2, 3], target = 10 -&gt; None

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：1000 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/10-two-sum/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/two-sum:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{10_4dddd9c16c01b09bea397b239035ab9c}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

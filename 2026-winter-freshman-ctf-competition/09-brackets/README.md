# 09 · 括号校验

### 作者
aipno

### 方向
Python

### 知识点
用列表实现栈、括号匹配、最大嵌套深度

### 难度
困难（9/10）

### 内容
实现 solve(case)，检查 case["text"] 中的括号是否配对，返回 [是否合法, 最大嵌套深度]。

文本只包含三种括号：()、[]、{}，没有其他字符。

- 类型必须一一对应，"(]" 和 "([)]" 都不合法
- 合法时深度是扫描过程中栈的最大高度；空串合法，深度为 0
- 不合法时返回 [False, 0]

示例：
"()" -&gt; [True, 1]
"{[()]}" -&gt; [True, 3]
"([)]" -&gt; [False, 0]
"(]" -&gt; [False, 0]

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：Python 判题（容器题）；比赛分值：900 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/09-brackets/` 的原始题目。
- 归档：`attachment/solution.py` 是发给选手的骨架；`src/challenge/` 含 `meta.json`、`skeleton.py`、`checker.py`、`reference.py`。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/brackets:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{09_53ba94112820350b03659c87c9a81a56}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

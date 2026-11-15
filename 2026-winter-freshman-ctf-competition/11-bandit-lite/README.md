# 11 · Bandit-lite：五关小迷宫

### 作者
aipno

### 方向
终端

### 知识点
隐藏文件、chmod、软链接、base64、带空格文件名

### 难度
中等（5/10）

### 内容
一台隔离的 Linux 沙箱，地下有五层。每一关都会留下下一关的线索；最终 token 被拆成 part1、part2、part3，level5 里写着拼接规则。

把拼出来的 32 位十六进制 token 填到下方输入框，领取 flag。

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：交互式终端（容器题）；比赛分值：500 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/11-bandit-lite/` 的原始题目。
- 归档：`src/challenge/` 含 `meta.json` 和场景生成器 `scene.py`；没有选手附件，选手在浏览器终端里操作。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/bandit-lite:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{11_7da90781780fac41d302a73b}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

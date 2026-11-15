# 12 · 进程猎手

### 作者
aipno

### 方向
终端

### 知识点
ps、/proc/&lt;pid&gt;/fd、已删除但仍打开的文件

### 难度
中等（6/10）

### 内容
沙箱里有三个长期运行的后台进程。其中一个进程手里还拿着本题的 token：那份文件已经从目录里消失，但还没有真正离开系统。

找到 token=... 的值，提交到网页。

注意：不要重启或杀掉这些进程，否则线索会永久丢失。
这道题考的是 Linux 进程与文件的关系，不是提权。

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：交互式终端（容器题）；比赛分值：580 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/12-proc-hunt/` 的原始题目。
- 归档：`src/challenge/` 含 `meta.json` 和场景生成器 `scene.py`；没有选手附件，选手在浏览器终端里操作。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/proc-hunt:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{12_2b9a70257d8a81a3bdac7307}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

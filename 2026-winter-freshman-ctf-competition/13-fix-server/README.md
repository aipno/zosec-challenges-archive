# 13 · 修好这个站点

### 作者
aipno

### 方向
终端

### 知识点
文件权限、config.ini、后台进程、curl、loopback 服务

### 难度
中等（7/10）

### 内容
沙箱里有一个坏掉的静态站点：服务起不来，健康检查也不通过。TASK.md 里写着本次会话的 SITE_PORT、SITE_ROOT 和 GATE_PORT。

把它修好、在后台跑起来，然后访问 http://127.0.0.1:&lt;GATE_PORT&gt;/token 领取 token 并提交。
健康检查的 checks 字段会逐项告诉你还差什么。

### 提示
无。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：交互式终端（容器题）；比赛分值：660 分。
- 来源：原项目 `competitions/2026-winter-freshman-ctf-competition/13-fix-server/` 的原始题目。
- 归档：`src/challenge/` 含 `meta.json` 和场景生成器 `scene.py`；没有选手附件，选手在浏览器终端里操作。
- 本地镜像：`docker.iswxl.cn/aipno/2026-winter-freshman-ctf-competition/fix-server:archive`（`docker.iswxl.cn`，匿名可拉取），运行命令见 [`env/README.md`](env/README.md)。
- Flag 说明：比赛时平台为每个实例注入动态 flag；下面是本地复现用 flag。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{13_f2743f76386e24793f64870f}`

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

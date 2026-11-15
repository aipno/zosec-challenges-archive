# 12 · 进程猎手 — Writeup

## 步骤

先看当前用户运行的进程：

```bash
ps -ef
# 或
ps aux
```

会看到三个长期运行的进程，名字在 `backup-agent`、`sync-worker`、`log-shipper` 之间随机分配，命令类似：

```text
<uid>  ...  backup-agent 3600
```

三个进程里只有一个拿着真正的 token，另外两个是诱饵。不要杀掉进程——进程一退出，它打开的文件描述符就消失了。

对每个 PID 检查打开的文件：

```bash
ls -l /proc/<pid>/fd
```

其中一个 fd 指向一个带 `(deleted)` 标记的路径，例如：

```text
lrwx------ 1 ... /proc/1234/fd/3 -> /home/.../.victim-xxxx (deleted)
```

找到 `(deleted)` 对应的 fd 编号后读取它：

```bash
cat /proc/<pid>/fd/<fd>
```

三个进程都读一遍，只有一份内容是 `token=<32 位十六进制>`，其余是 `not the token (decoy ...)`。把 token 填到网页输入框。

## 原理

`src/challenge/scene.py` 只定义进程名和 token，broker 负责启动这些进程：它创建一个临时文件，写入 token（或诱饵），把只读 fd 传给 `sleep` 进程，然后 `unlink` 文件。文件从目录里消失，但 inode 还被进程的 fd 持有，所以能从 `/proc/<pid>/fd/<n>` 读回来。这是 Linux 上“已删除但仍打开”的经典现象。

## Flag

`flag{12_2b9a70257d8a81a3bdac7307}`

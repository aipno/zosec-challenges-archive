# 13 · 修好这个站点 — Writeup

## 步骤

先读任务参数：

```bash
cat TASK.md
. ./.task-env
```

`.task-env` 里有本次会话的 `SITE_PORT`、`SITE_ROOT`、`GATE_PORT`。

### 1. 修复执行权限和可读权限

```bash
chmod +x server/run.sh
chmod 644 site/health.txt
```

`run.sh` 初始是 `0644`，不能执行；`site/health.txt` 初始是 `000`，站点进程读不到。

### 2. 修改 config.ini

把 host 改成 loopback，port 和 root 改成任务参数：

```bash
sed -i 's/^host = .*/host = 127.0.0.1/' server/config.ini
sed -i "s/^port = .*/port = $SITE_PORT/" server/config.ini
sed -i "s|^root = .*|root = $SITE_ROOT|" server/config.ini
```

确认结果：

```bash
cat server/config.ini
```

应当是：

```ini
[server]
host = 127.0.0.1
port = <SITE_PORT>
root = <SITE_ROOT>
```

### 3. 在后台启动站点

```bash
nohup ./server/run.sh >server.log 2>&1 &
sleep 1
cat server.log
```

`site_server.py` 会在 `127.0.0.1:<SITE_PORT>` 提供静态文件，并在 `/health.txt` 响应里带上 `X-Health-Marker` 头。

### 4. 向 gate 领 token

```bash
curl "http://127.0.0.1:$GATE_PORT/token"
```

成功时返回：

```json
{"ok": true, "token": "..."}
```

把 token 填到网页输入框。如果返回 403，读 `checks` 字段：

```json
{"ok": false, "checks": {"run_executable": true, "config": false, "health_file": true, "site_server": false}}
```

逐项对照：`run_executable`（run.sh 执行位）、`config`（host/port/root）、`health_file`（health.txt 可读且内容等于 gate 的随机 marker）、`site_server`（你的站点能返回 marker 和 `X-Health-Marker` 头）。

## 注意

- 必须用题目自带的 `server/site_server.py`（或自己实现同样的 `X-Health-Marker` 头）；裸 `python3 -m http.server` 不会带这个头，`site_server` 检查会失败。
- 不要杀掉 gate；它是 broker 里的 root 线程，token 只在内存里。
- 页面返回 403 是正常的中间状态，按 `checks` 修即可。

## 原理

`src/challenge/scene.py` 生成坏掉的站点、随机 token 和 marker；gate 在 broker 里检查四项条件，全部满足才返回 token。这是“文件权限 + 配置 + 后台进程 + 本地 HTTP 服务”的综合练习，不涉及提权。

## Flag

`flag{13_f2743f76386e24793f64870f}`

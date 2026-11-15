# 19 · 运维小站 — Writeup

## 思路

信息搜集两步：

1. 访问 `/robots.txt`，看到 `Disallow: /secret-panel/`；
2. 访问 `/secret-panel/`，查看网页源代码，底部 HTML 注释里有 `面板访问令牌 = flag{...}`。

```bash
curl -s http://127.0.0.1:8126/robots.txt
curl -s http://127.0.0.1:8126/secret-panel/ | grep -o 'flag{[^}]*}'
```

## 原理

`src/app/app.py` 的 `robots()` 故意把隐藏路径写进 `robots.txt`；`src/app/templates/c1_panel.html` 在 HTML 注释里渲染 `{{ flag }}`。页面正文没有 flag，只有源码注释里有。

## Flag

`flag{0e7f41bf26743dc8adb81bbe0a0a8328}`（本地复现 flag；平台实例的 flag 由 `FLAG` 环境变量注入）

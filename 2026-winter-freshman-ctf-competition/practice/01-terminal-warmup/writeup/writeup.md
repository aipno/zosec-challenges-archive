# 01 · 终端热身：隐藏文件里的 token — Writeup

## 步骤

连接终端后，先列出包括隐藏文件在内的目录内容：

```bash
ls -la
```

会看到一个以 `.` 开头的 `.welcome`。读取它：

```bash
cat .welcome
```

文件里有一行 `token=<32 位十六进制>`，把等号后面的值填到网页输入框即可。

## 原理

`src/challenge/scene.py` 每次会话用 `secrets.token_hex(16)` 生成随机 token，写入 `.welcome`；broker 在内存里保存期望值，网页只负责校验并返回 flag。所以 token 不能从其他会话复用。

## Flag

`flag{01_b56ae2d50665b22c5daeef66}`

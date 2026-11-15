# 16 · 被 XOR 过的秘密 — Writeup

## 思路

单字节 XOR 的密钥只有一个字节。已知明文以 `flag{` 开头，所以：

```text
cipher[0] ^ ord("f") = key
```

`cipher[0]` 是 `0x4c`，`ord("f")` 是 `0x66`，所以密钥是 `0x2a`。把整个文件逐字节 XOR `0x2a` 即可。

```python
from pathlib import Path

data = Path("attachment/encrypted-001.bin").read_bytes()
key = data[0] ^ ord("f")
print(f"key = {key:#x}")
print(bytes(b ^ key for b in data).decode())
```

## 一行命令

```bash
python3 -c 'import pathlib; data=pathlib.Path("attachment/encrypted-001.bin").read_bytes(); key=data[0]^ord("f"); print(bytes(b^key for b in data).decode())'
```

## 为什么不是别的密钥

也可以暴力枚举 0–255，检查解出来的文本是否以 `flag{` 开头；已知明文让这一步变得不必要。`src/challenge/content.py` 固定使用 `KEY = 0x2A` 生成整份附件。

## Flag

`flag{7598e3bec2d64ef632db021ac711154f}`（样例附件 `encrypted-001.bin`；完整 50 个 flag 见 `flags.txt`）

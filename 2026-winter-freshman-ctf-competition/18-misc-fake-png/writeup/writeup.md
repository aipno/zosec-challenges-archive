# 18 · 打不开的图片 — Writeup

## 思路

文件开头是合法的 PNG 签名：

```text
89 50 4e 47 0d 0a 1a 0a
```

但签名之后不是 PNG 数据块，而是普通文本。用 `xxd` 看字节，或直接 `strings`：

```bash
xxd attachment/image-001.png | head
strings attachment/image-001.png | grep -o 'flag{[^}]*}'
```

`xxd` 输出里能看到 `fake png data padding...` 和明文 flag；`strings` 会直接打印出来。

## 原理

`src/challenge/content.py` 的 `build(flag)` 只写入 PNG 魔术数、填充文本、flag 和尾部填充。它不是一张能解码的 PNG，所以看图软件会报错；flag 就藏在签名后的明文里。

## Flag

`flag{a467929a9473f89f9c32c3ed426868c1}`（样例附件 `image-001.png`；完整 50 个 flag 见 `flags.txt`）

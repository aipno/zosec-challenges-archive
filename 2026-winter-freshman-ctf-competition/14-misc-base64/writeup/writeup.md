# 14 · 一张奇怪的纸条 — Writeup

## 思路

`attachment/secret-001.txt` 有三行，都是 Base64。把每一行分别解码，只有中间那行是 flag。

```python
import base64
from pathlib import Path

lines = Path("attachment/secret-001.txt").read_text().splitlines()
for i, line in enumerate(lines, 1):
    print(i, base64.b64decode(line).decode())
```

输出类似：

```text
1 Hello world! This is just a test.
2 flag{...}
3 Good luck on your CTF practice!
```

第一行和第三行是干扰文本。`src/challenge/content.py` 的 `build(flag)` 会把 flag 做 Base64 后放在第二行。

## 一行命令

```bash
python3 -c 'import base64, pathlib; print(base64.b64decode(pathlib.Path("attachment/secret-001.txt").read_text().splitlines()[1]).decode())'
```

## Flag

`flag{bd665776a3af17eb5f8b5249ab26304d}`（样例附件 `secret-001.txt`；完整 50 个 flag 见 `flags.txt`）

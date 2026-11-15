# 15 · 罗马将军的笔记 — Writeup

## 思路

笔记是 ROT13：每个字母向后/向前平移 13 位，大小写保持。第二行 `Gur frperg pbqr vf ...` 解码后是 `The secret code is flag{...}`。

```python
import codecs
from pathlib import Path

text = Path("attachment/note-001.txt").read_text()
print(codecs.decode(text, "rot_13"))
```

输出：

```text
These ciphers are $< Nice today?
The secret code is flag{...}
Hint: the ancient roman general loved shifting letters.
```

最后一行也直接提示了“罗马将军”和“移位字母”。

## 一行命令

```bash
python3 -c 'import codecs, pathlib; print(codecs.decode(pathlib.Path("attachment/note-001.txt").read_text(), "rot_13"))'
```

## Flag

`flag{b44a2cf56d06d77ff50ee1166a7f3051}`（样例附件 `note-001.txt`；完整 50 个 flag 见 `flags.txt`）

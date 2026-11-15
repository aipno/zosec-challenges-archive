# 16 · 被 XOR 过的秘密

### 作者
aipno

### 方向
Crypto

### 知识点
单字节 XOR、已知明文攻击

### 难度
简单（2/10）

### 内容
一个二进制文件，内容被同一个单字节密钥 XOR 过。你知道所有明文都以 `flag{` 开头。

下载分到的 encrypted-*.bin，还原出完整的 flag。

### 提示
- 已知明文的第一段，就够反推出整把钥匙。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：动态附件（无容器）；比赛分值：300 分。
- 来源：原题来自项目根目录 `ctf-practice.zip` → `challenge3-crypto/encrypted.bin`，在 `zips/16-crypto-xor/` 中改写为动态附件池。
- 归档：`attachment/encrypted-001.bin` 是 50 份附件中的 1 份样例；`flags.txt` 是完整 flag 列表；`src/challenge/` 含 `meta.json` 和附件生成器 `content.py`。
- Flag 说明：本题使用 50 个动态 flag，每份附件对应一个；下面是样例附件的 flag，完整列表在 `flags.txt`。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{7598e3bec2d64ef632db021ac711154f}`（样例附件 `encrypted-001.bin`）
- 其余 49 个 flag 见 [`flags.txt`](flags.txt)。

<details>
<summary>展开全部 50 个 flag</summary>

- `flag{7598e3bec2d64ef632db021ac711154f}`
- `flag{6c8b78849b73b77b75ace4e21cba4562}`
- `flag{c229cb64b9a6ddb1218682d1c30090fe}`
- `flag{9de08298912596465c2fe9bb078a2bc3}`
- `flag{2f997444eb18d280bc5302082f85dda0}`
- `flag{f66204978ecdf2d4bb9fce0f9be1c052}`
- `flag{cffe3fd189020144154bf7edd6110582}`
- `flag{3a3d512154fddfdb99a14da890da13c3}`
- `flag{6558dfd9775a767b03c872a151e69c87}`
- `flag{6805e156b4d2493308cba6b8b3331c5c}`
- `flag{00dccbc0d5ea6ecdd4f6cb0e2cbb8f1f}`
- `flag{c53fffbd1e238f4a1504568a2e385e76}`
- `flag{4e39893ac42ce8ea2c5454da23daa92a}`
- `flag{bc65b76abc79f65c841b14ea11bb0685}`
- `flag{67837663c8292202d7e439e24d1cf79f}`
- `flag{4886f0c44d0a2b77cb174deaeb081d14}`
- `flag{ba93efb4cdfac91848af80beb46ecc82}`
- `flag{268dad45d635b42671ec7e8fd0c40b9f}`
- `flag{365fc12a34623aa55fcb3483fbdac94a}`
- `flag{329a3e2cdc51a1ce3e4b3009fd7b3b14}`
- `flag{74c1141b4b2d69f66e098e60ebd1d7cd}`
- `flag{2149aa00becab66e961a9f6f69d021ae}`
- `flag{9f56038b7bbfce0823b2aef2eddbf950}`
- `flag{866a7d42460343dc5324b520ba8b72e4}`
- `flag{91fc89b5bea8e702a8a1dff0302da97a}`
- `flag{f60bce10bc33c39b838a3869cbd39109}`
- `flag{dfb5fe95e703bf753bb260eae692a9b9}`
- `flag{63edfdfb20fcfc4e0f5594413bab2065}`
- `flag{7985649206307046c8644635933654b9}`
- `flag{728dc4a57ffd758c016bdb45769c07a8}`
- `flag{e4355be33df6e86e8e07690f5056844a}`
- `flag{0a70c535864e2aa6e990288d9e5057cd}`
- `flag{a46e85dc5b0ffa09c2ab29df5e2f1fb4}`
- `flag{67feeeaa66d600aadfe8d974cab28931}`
- `flag{bcf56200ea4742892f923d62776a9254}`
- `flag{a4992ed475b36bfdbf2021d20d9efa1c}`
- `flag{20eb446cf15351df794b11a2414e3c65}`
- `flag{2f2ae2b260b366abaf9beb61bd6f1696}`
- `flag{e115f5536318e8078299b98fbb3ed248}`
- `flag{a0f6870cbf0408673050eb63ede7a4be}`
- `flag{a5f120ebac3588023c03b26e9b45035c}`
- `flag{3f1789b52b5b5b4bf0c8125c4d13b70f}`
- `flag{3b6d53b55ddf282d533bbca02027499d}`
- `flag{1a35d46b10b3352aec9a8bdadd7baec2}`
- `flag{9b1ebe38b0dc5c827d756c31e1b7433c}`
- `flag{2c7dea91f5b12ad86cc42d220c4594bf}`
- `flag{38bc7edf8d44142a27b793c7b15c59cd}`
- `flag{b62c24b8f8cafb7ff54331259b760e9c}`
- `flag{6d10287a0cf134037c632158bbe4bb51}`
- `flag{0b608fdf51f975645015c230bbbab769}`

</details>

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

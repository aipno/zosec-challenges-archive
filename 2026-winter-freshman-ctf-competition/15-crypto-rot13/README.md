# 15 · 罗马将军的笔记

### 作者
aipno

### 方向
Crypto

### 知识点
ROT13 移位密码

### 难度
简单（1/10）

### 内容
一张古代笔记，字迹清楚，但读起来像另一种语言。

下载分到的 note-*.txt，还原出隐藏的 flag。

### 提示
- 字母被整体平移过，平移量是固定的；从 0 试到 25 总能撞到。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：动态附件（无容器）；比赛分值：200 分。
- 来源：原题来自项目根目录 `ctf-practice.zip` → `challenge2-crypto/note.txt`，在 `zips/15-crypto-rot13/` 中改写为动态附件池。
- 归档：`attachment/note-001.txt` 是 50 份附件中的 1 份样例；`flags.txt` 是完整 flag 列表；`src/challenge/` 含 `meta.json` 和附件生成器 `content.py`。
- Flag 说明：本题使用 50 个动态 flag，每份附件对应一个；下面是样例附件的 flag，完整列表在 `flags.txt`。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{b44a2cf56d06d77ff50ee1166a7f3051}`（样例附件 `note-001.txt`）
- 其余 49 个 flag 见 [`flags.txt`](flags.txt)。

<details>
<summary>展开全部 50 个 flag</summary>

- `flag{b44a2cf56d06d77ff50ee1166a7f3051}`
- `flag{64aad894eccb7ed18035b5100e820dde}`
- `flag{d338ab96c932ab403425a0c982c81ab2}`
- `flag{5b6fa9115a063dfd5a24bd736e3d0d4f}`
- `flag{2f61c4386cf405fa76d6ef5bbe9093e7}`
- `flag{124926935300c66fb019f14b6612889a}`
- `flag{1794ef0b11be8ccff8a3cc86df4638da}`
- `flag{fb15836c4943c11f4662cbad77f42f45}`
- `flag{55aaf27c661ce52c83b1b161744c6524}`
- `flag{55addfe9981309f3b9375116cc2fdd65}`
- `flag{207cf0ae8484a4484b91304c26c6aa44}`
- `flag{a1cdd48c88040536ae55d7aacf194dec}`
- `flag{d173137dbbcf1c8712d9a8dc3a74fa36}`
- `flag{c0cc2c3d5c3082228bcd4687a9055fd2}`
- `flag{c0b4a6a4aba8ad3939c2911fc9a1c5cf}`
- `flag{bc99d7c6e623812756482cb8701936af}`
- `flag{c6f6c09dfa8a8304c3750140fe3ba512}`
- `flag{a9e73919cac4b1ae32c3808e9640f30f}`
- `flag{fc22af77ff28d9ec16e184582227d7c5}`
- `flag{ebe444156a70ad8d2d1eeb1845b689a0}`
- `flag{29d11e10e1332965354dd9826599670b}`
- `flag{691e996b80b7292439bdd43dd2ae1611}`
- `flag{275303da8366059c6d84e375b798a6ed}`
- `flag{2ae1470c03ea10f611a4960a625e4eb1}`
- `flag{96de1ab7239abfb9ecd4d78ef1707385}`
- `flag{5f707d249ec4a51152dc9e29d47e9ecc}`
- `flag{e6866b1f9816b911caa63952ad95339a}`
- `flag{5d863f13e245251281202dd8a3693578}`
- `flag{2608218aa9d0c253745b49f4bd120f16}`
- `flag{7bf8555a8d20aa8f23f115ab66f697ab}`
- `flag{09e5c50e969e98bf85499e671bf9a50d}`
- `flag{c04d91a15c4bfcaed2069de7bffbf580}`
- `flag{49fb253d105fcfeeb6e656532e596d20}`
- `flag{1e70604b93671ba2170fa7a483162523}`
- `flag{73ab8f7e6a2524618f434e4543526389}`
- `flag{108c6191b095b650fc50da7d8e7aaa64}`
- `flag{8c9b1ddab9f7d2a80d8a1dbb565cc3dc}`
- `flag{fb916bdaaf6f876bbd5b978d419cb442}`
- `flag{a33531b6475047ee891af5328b422b39}`
- `flag{142ffedaed465b8becd5b12b102021dc}`
- `flag{981ab400f2b1e87e15af5e27cb24f297}`
- `flag{edecd996140a512e245a3379a45f6ae2}`
- `flag{3ad9f6e3feabe300d37ab05f94a52a70}`
- `flag{4cb2377422fa8ed722001b659c41a973}`
- `flag{a5ef54edc7ab766cd31b607b798c034f}`
- `flag{f4ecdb5611f4e32e87970b7f4a5f0f3b}`
- `flag{86880feb8d1c89e54724c39fc8e28909}`
- `flag{729c721e9e22673099f9a9d6ddf22f4e}`
- `flag{76fc113ec7d3940d2bb3e51e52502790}`
- `flag{bdbd482233d3ddc25e15f5fcb6f9a789}`

</details>

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

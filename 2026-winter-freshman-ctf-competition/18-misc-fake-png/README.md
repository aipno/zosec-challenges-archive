# 18 · 打不开的图片

### 作者
aipno

### 方向
Misc

### 知识点
文件签名、xxd / strings

### 难度
简单（2/10）

### 内容
朋友发来一张「图片」，但任何看图软件都打不开它。

下载分到的 image-*.png，从文件里找出 flag。

### 提示
- 别只看内容——文件的字节结构本身就有问题。

### 是否可共享
是。本目录是赛后公开归档，可直接用于学习与复盘。

### 备注
- 题型：动态附件（无容器）；比赛分值：260 分。
- 来源：原题来自项目根目录 `ctf-practice.zip` → `challenge5-misc/image.png`，在 `zips/18-misc-fake-png/` 中改写为动态附件池。
- 归档：`attachment/image-001.png` 是 50 份附件中的 1 份样例；`flags.txt` 是完整 flag 列表；`src/challenge/` 含 `meta.json` 和附件生成器 `content.py`。
- Flag 说明：本题使用 50 个动态 flag，每份附件对应一个；下面是样例附件的 flag，完整列表在 `flags.txt`。
- 运行环境需自行搭建；平台前端、judge/broker、Docker/compose、构建脚本和测试不在归档范围内。

### FLAG
- `flag{a467929a9473f89f9c32c3ed426868c1}`（样例附件 `image-001.png`）
- 其余 49 个 flag 见 [`flags.txt`](flags.txt)。

<details>
<summary>展开全部 50 个 flag</summary>

- `flag{a467929a9473f89f9c32c3ed426868c1}`
- `flag{35b5bf2344208191024b9a60ab63bf7e}`
- `flag{d68d864c2e5c550cd16da08ec5cdccd4}`
- `flag{583b95132bc608d20736130694b7300b}`
- `flag{96cbf9a65bdbb95332afdab770d985f7}`
- `flag{1f1452fc1d1a8ad5db4de9438c189136}`
- `flag{0cc8871c1a97c2c3a861956dbfa9ed45}`
- `flag{3af4fe0047ec7d5806af000853112e09}`
- `flag{afd41695fcfb27766059f839e272662d}`
- `flag{d07e49ba0960b952fb8a30d28e1e9cba}`
- `flag{656310f4f06d10b092a280c5cb5189e4}`
- `flag{42e313199f02dde8cb05d2fbd75ae73e}`
- `flag{444db7d8ae6a9e538df5e31300a7aaf0}`
- `flag{dcb588f62fbaff86ba5bbf3c06690253}`
- `flag{a7b5bb25bd384e9f6dcfba2dca73d893}`
- `flag{3724275e78218eebf3754d5727045579}`
- `flag{02ad96db5896edfb95d73393a856c919}`
- `flag{899cdc0a728f600c1bbf68664616da01}`
- `flag{0ace88a72635265c81b567425ad7a085}`
- `flag{7025d671342b123cfa368da6d3ae1a63}`
- `flag{a8b4bcf2c969afef87424a249f1b85f4}`
- `flag{e4ecd6b2bf13c0f0748a528f73658196}`
- `flag{0ed8eb5ba33e28b5a9b30b6ac62c1025}`
- `flag{a6fd7c76eb07d73436ea2972fd5e807a}`
- `flag{19bdd0bddcbb8fea68fff781fbf76075}`
- `flag{1a572cafc9641b7ef00438dae6c460a8}`
- `flag{40d379b2a8fd711cf7396f547bf0068a}`
- `flag{643105e601ee9f8ff3e3e3e2bd46b5c6}`
- `flag{30ec16ef64e14f6b9ae0f742ae45c8e9}`
- `flag{aae07c524c87e192e94f0b85f522e1ef}`
- `flag{404dcac39bda576e8e22489a5a11f3ce}`
- `flag{9a79dd5d7d42516239cb5a0a09df38db}`
- `flag{7fbc3fa6d9b48181333549a48611e86c}`
- `flag{99c17f6387f2680420b4f0def3c821ef}`
- `flag{47044003c85165bf47a5db3d6bc4e0e5}`
- `flag{8c5147fd1afda67ea8275407206b4332}`
- `flag{9ef3cfd8eab7ae1a6a195759554d94ac}`
- `flag{bd6ac69054efbdda1da3aa502188a217}`
- `flag{832f82733355ec9d11bb13686462de76}`
- `flag{96a78ec3382ed47cef5f91d039537dc6}`
- `flag{ec211b05cbfb16fd26c5b6e82fe4dca3}`
- `flag{690e21b832408ef5e84c721b5311126b}`
- `flag{e2ae597e226d1802bfa100bdb2d9dcc2}`
- `flag{f636afcbfbecdbbf0f2d9def4c6e0dda}`
- `flag{6beaab82b893939539ea0f4cb8ab4f35}`
- `flag{0159c708798347370a26d33fb11f4b47}`
- `flag{b4c541aaeded83e8f4f9389df67d555c}`
- `flag{5f7c224ed41791ee531fd348635b1c7f}`
- `flag{5a3ae940dc60801231769d6d9816be0b}`
- `flag{147ba9423bda2fbc7abda7abb6247f20}`

</details>

## 题解

见 [`writeup/writeup.md`](writeup/writeup.md)。

# 11 · Bandit-lite：五关小迷宫 — Writeup

## 步骤

从 `level1/README` 开始，逐关拿 `part1`、`part2`、`part3`。

### 第 1 关：隐藏文件

```bash
ls -la
cat level1/.hint
```

`.hint` 不在普通 `ls` 的结果里，`ls -la` 才能看到。里面给出 `part1=...`。

### 第 2 关：权限

```bash
chmod 600 level2/secret
cat level2/secret
```

`secret` 初始是 `000`，作为属主可以自己 `chmod` 后再读。里面给出 `part2=...`。

### 第 3 关：软链接

```bash
readlink -f level3/link
```

`level3/link` 指向 `../level4/.cipher`。`readlink -f` 会解析成绝对路径。

### 第 4 关：Base64

```bash
base64 -d "$(readlink -f level3/link)"
```

解码后得到 `part3=...` 和下一关提示。

### 第 5 关：带空格的文件名

```bash
cat "level5/with space.txt"
```

文件名里有空格，必须加引号（或用 `\ ` 转义）。文件里写着拼接规则。

### 拼接并提交

把三段从输出里提取到变量：

```bash
part1=$(grep -o 'part1=[0-9a-f]*' level1/.hint | cut -d= -f2)
part2=$(grep -o 'part2=[0-9a-f]*' level2/secret | cut -d= -f2)
part3=$(base64 -d "$(readlink -f level3/link)" | grep -o 'part3=[0-9a-f]*' | cut -d= -f2)

token="${part1}${part2}${part3}"
echo "$token"
```

把 32 位十六进制 token 填到网页输入框，领取 flag。`part1` 长 11 位、`part2` 长 11 位、`part3` 长 10 位，拼起来正好 32 位。

## 原理

`src/challenge/scene.py` 每次会话随机生成 token，拆成三段散在 level1/2/4；level5 只放拼接规则，所以 `grep token` 或 `cat level5/*` 拿不到完整答案。broker 在内存里保存完整 token。

## Flag

`flag{11_7da90781780fac41d302a73b}`

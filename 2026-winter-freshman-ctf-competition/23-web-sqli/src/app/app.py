"""23 · SQL 注入：字符串拼接导致的管理员登录绕过。"""

from __future__ import annotations

import os
import secrets
import sqlite3
from pathlib import Path

from flask import Flask, g, render_template, request

from common.flags import load_flag
from common.metadata import load_meta
from common.web import configure, template_loader

META = load_meta()
FLAG = load_flag()

APP_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(APP_DIR / "templates"), static_folder=None)
app.jinja_loader = template_loader(APP_DIR)
configure(app, FLAG, META)

PAGE_TITLE = "会员登录"
PAGE_TAG = META["tag"]

# /tmp is a tmpfs in the platform compose file; the image itself is read-only
# in that mode.  A plain `docker run` also has a writable /tmp.
DB_PATH = os.environ.get("DB_PATH", "/tmp/app.db")


def init_db() -> None:
    """Create the small user table; safe to call on every process start."""

    directory = os.path.dirname(DB_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    try:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT NOT NULL,
                passwd  TEXT NOT NULL,
                role    TEXT NOT NULL DEFAULT 'user'
            )
            """
        )
        # The admin password is random and is never printed or stored in the
        # image.  The intended way in is the SQL injection below; a weak
        # credential such as admin888 must not work.  The update also covers
        # /tmp/app.db left behind by an older process in the same container.
        admin_password = secrets.token_urlsafe(32)
        if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
            db.executemany(
                "INSERT INTO users (name, passwd, role) VALUES (?, ?, ?)",
                [
                    ("admin", admin_password, "admin"),
                    ("guest", "guest", "user"),
                    ("tester", "test123", "user"),
                ],
            )
        db.execute(
            "UPDATE users SET passwd = ? WHERE name = 'admin'",
            (admin_password,),
        )
        db.commit()
    finally:
        db.close()


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


init_db()


def render_login(**kwargs):
    return render_template(
        "c5_login.html",
        title=PAGE_TITLE,
        tag=PAGE_TAG,
        **kwargs,
    )


@app.get("/")
def index():
    return render_login()


@app.post("/login")
def login():
    name = request.form.get("name") or ""
    passwd = request.form.get("passwd") or ""

    # Intentionally vulnerable: the values are concatenated into SQL.  This
    # is the teaching point of the challenge; do not "fix" it here.
    sql = (
        "SELECT id, name, role FROM users "
        f"WHERE name = '{name}' AND passwd = '{passwd}'"
    )
    try:
        rows = get_db().execute(sql).fetchall()
    except sqlite3.Error as exc:
        # Echo the database error so beginners can see how the query broke.
        return render_login(error=f"数据库错误：{exc}")

    if not rows:
        return render_login(error="用户名或密码错误")

    row = rows[0]
    is_admin = row["role"] == "admin"
    return render_login(
        ok=True,
        user=row["name"],
        role=row["role"],
        flag=FLAG if is_admin else None,
        msg="登录成功" + ("（管理员）" if is_admin else "（普通用户，无权查看 flag）"),
    )


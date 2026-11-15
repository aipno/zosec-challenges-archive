"""21 · 爆破（一）：后台登录弱口令（无锁定、无验证码）。"""

from __future__ import annotations

import os
import secrets
from pathlib import Path

from flask import Flask, render_template, request, session

from common.flags import load_flag
from common.metadata import load_meta
from common.web import configure, template_loader

META = load_meta()
FLAG = load_flag()

APP_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(APP_DIR / "templates"), static_folder=None)
app.jinja_loader = template_loader(APP_DIR)
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)
configure(app, FLAG, META)

PAGE_TITLE = "管理后台登录"
PAGE_TAG = META["tag"]
USERNAME = "admin"
PASSWORD = "admin888"


def render_login(*, logged: bool, msg: str = "", flag: str | None = None):
    return render_template(
        "c3_login.html",
        title=PAGE_TITLE,
        tag=PAGE_TAG,
        logged=logged,
        msg=msg,
        flag=flag,
    )


@app.get("/")
def index():
    logged = bool(session.get("logged_in"))
    return render_login(
        logged=logged,
        msg="登录成功，欢迎回来，管理员。" if logged else "",
        flag=FLAG if logged else None,
    )


@app.post("/login")
def login():
    username = (request.form.get("username") or "").strip()
    password = request.form.get("password") or ""

    if username == USERNAME and password == PASSWORD:
        session["logged_in"] = True
        return render_login(
            logged=True,
            msg="登录成功，欢迎回来，管理员。",
            flag=FLAG,
        )

    # Deliberately does not distinguish "unknown user" from "wrong password",
    # and has no lockout or rate limit: that is the challenge.
    return render_login(logged=False, msg="用户名或密码错误")

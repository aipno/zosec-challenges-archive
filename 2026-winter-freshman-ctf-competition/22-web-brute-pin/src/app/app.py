"""22 · 爆破（二）：4 位数字 PIN，带每秒 800 次的失败限速。"""

from __future__ import annotations

import threading
import time
from pathlib import Path

from flask import Flask, render_template, request

from common.flags import load_flag
from common.metadata import load_meta
from common.web import configure, template_loader

META = load_meta()
FLAG = load_flag()

APP_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(APP_DIR / "templates"), static_folder=None)
app.jinja_loader = template_loader(APP_DIR)
configure(app, FLAG, META)

PAGE_TITLE = "支付密码验证"
PAGE_TAG = META["tag"]

CORRECT_PIN = "2846"

# Only failed attempts are limited.  A correct PIN is always accepted, even
# when the failure window is full; otherwise a brute-force script could miss
# the answer at the moment it happens to be rate-limited.
_MAX_FAILURES_PER_SECOND = 800
_failures: list[float] = []
_failures_lock = threading.Lock()


def rate_limited() -> bool:
    now = time.monotonic()
    with _failures_lock:
        _failures[:] = [stamp for stamp in _failures if now - stamp < 1.0]
        if len(_failures) >= _MAX_FAILURES_PER_SECOND:
            return True
        _failures.append(now)
        return False


def render_pin(*, msg: str | None = None, flag: str | None = None):
    return render_template(
        "c4_pin.html",
        title=PAGE_TITLE,
        tag=PAGE_TAG,
        msg=msg,
        flag=flag,
    )


@app.get("/")
def index():
    return render_pin()


@app.post("/verify")
def verify():
    pin = (request.form.get("pin") or "").strip()

    # Check the answer before the failure limiter: the correct PIN must never
    # be blocked by earlier failed guesses.
    if pin == CORRECT_PIN:
        return render_pin(msg="支付密码正确", flag=FLAG)

    if rate_limited():
        return render_pin(msg="请求过于频繁，请稍后再试")

    return render_pin(msg="支付密码错误，请重新输入")

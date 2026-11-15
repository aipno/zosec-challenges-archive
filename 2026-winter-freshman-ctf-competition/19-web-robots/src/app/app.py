"""19 · 信息搜集（一）：robots.txt + 页面源码注释泄露 flag。"""

from __future__ import annotations

from pathlib import Path

from flask import Flask, render_template

from common.flags import load_flag
from common.metadata import load_meta
from common.web import configure, template_loader

META = load_meta()
FLAG = load_flag()

APP_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=str(APP_DIR / "templates"), static_folder=None)
app.jinja_loader = template_loader(APP_DIR)
configure(app, FLAG, META)

PAGE_TITLE = "运维小站"
PAGE_TAG = META["tag"]


@app.get("/")
def index():
    return render_template("c1_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/status")
def status():
    return render_template("c1_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/docs")
def docs():
    return render_template("c1_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/internal/")
def internal():
    return render_template("c1_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/secret-panel/")
def secret_panel():
    return render_template(
        "c1_panel.html", title="内部面板", tag=PAGE_TAG, flag=FLAG
    )


@app.get("/robots.txt")
def robots():
    return (
        "User-agent: *\n"
        "Disallow: /secret-panel/\n"
        "Disallow: /internal/\n"
    )

"""20 · 信息搜集（二）：.git 目录 + 目录列表 + 备份文件泄露。"""

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

PAGE_TITLE = "MiniShop 商城"
PAGE_TAG = META["tag"]

BACKUP = f"""<!doctype html>
<html><head><title>index.html.bak</title></head>
<body>
<h1>MiniShop v1.0</h1>
<p>TODO: 下线前记得删除这个备份文件</p>
<!-- db password: shop123456 -->
<!-- admin token: {FLAG} -->
</body></html>
"""

GIT_CONFIG_FILE = """[core]
\trepositoryformatversion = 0
\tbare = false
\tlogallrefupdates = true
[remote "origin"]
\turl = https://github.com/ctf/minishop-demo.git
[branch "main"]
\tremote = origin
\tmerge = refs/heads/main
"""

GIT_HEAD = "ref: refs/heads/main\n"


@app.get("/")
def index():
    return render_template("c2_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/product")
def product():
    return render_template("c2_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/cart")
def cart():
    return render_template("c2_home.html", title=PAGE_TITLE, tag=PAGE_TAG)


@app.get("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /\n"


@app.get("/.git/HEAD")
def git_head():
    return GIT_HEAD


@app.get("/.git/config")
def git_config():
    return GIT_CONFIG_FILE


@app.get("/.git/")
def git_dir():
    return (
        "Index of /.git/\n\n"
        "<a href='/.git/HEAD'>HEAD</a>\n"
        "<a href='/.git/config'>config</a>\n"
    )


@app.get("/backup/")
def backup_dir():
    return (
        "Index of /backup/\n\n"
        "<a href='/backup/index.html.bak'>index.html.bak</a>\n"
    )


@app.get("/backup/index.html.bak")
def backup_file():
    return BACKUP


@app.get("/index.html.bak")
def backup_file2():
    return BACKUP

import os

from flask import *
from flask_flatpages import *
# from flask_frozen import Freezer
# from flaskext.markdown import Markdown
from pygments.formatters.html import HtmlFormatter
from werkzeug.exceptions import HTTPException

from . import app, flatpages
from config import *
from style import CustomMonokaiStyle
flatpages.init_app(app)
app.config["FLATPAGES_ROOT"] = os.path.join(app.root_path, "posts")
flatpages.reload()

from blog import blog_bp
from learning import learning_bp

app.register_blueprint(blog_bp)
app.register_blueprint(learning_bp)

app.logger.debug("url_map = %s", app.url_map)
app.logger.debug("prefix = %s", app.root_path)
app.logger.debug("flatpages_root = %s", app.config["FLATPAGES_ROOT"])
app.logger.debug("flatpages = %s", [p.path for p in flatpages])


@app.route('/pygments.css')
def pygments_css():
	style = HtmlFormatter(style=CustomMonokaiStyle).style
	return pygments_style_defs(style), 200, {'Content-Type': 'text/css'}


@app.errorhandler(Exception)
def handle_exception(e):
	if isinstance(e, HTTPException):
		return render_template("404.html"), e.code


@app.route("/")
def index():
	app.logger.debug("prefix = %s", g.url_prefix)
	return render_template('index.html')
	# _posts = sorted(
	# 	[p for p in flatpages if p.path.startswith("")],
	# 	key=lambda item: (not item["pinned"], item["date"])
	# )
	# return render_template("index.html", posts=_posts)

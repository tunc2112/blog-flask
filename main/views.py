import os
import traceback

from flask import *
from flask_flatpages import *
from pygments.formatters.html import HtmlFormatter
from werkzeug.exceptions import HTTPException

from . import app, flatpages
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
		return render_template("main/404.html"), e.code


@app.route("/")
def index():
	try:
		return render_template("main/index.html")
	except Exception:
		traceback.print_exc()
	# _posts = sorted(
	# 	[p for p in flatpages if p.path.startswith("")],
	# 	key=lambda item: (not item["pinned"], item["date"])
	# )
	# return render_template("index.html", posts=_posts)


@app.route("/search", methods=["GET", "POST"])
def search():
	# from forms import SearchForm
	# search_form = SearchForm()

	if request.method == "GET":
		query = request.args.get("s")
		results = []
		_posts = list(flatpages)
		for post in _posts:
			# TODO: Elastic search
			if post["category"].find(query) != -1 or any(tag.find(query) != -1 for tag in post["tags"])\
				or post["title"].find(query) != -1:
				results.append(post)

		results.sort(key=lambda item: (not item["pinned"], item["date"]))
		return render_template("blog/results.html", query=query, results=results)

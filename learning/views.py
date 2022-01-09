import os
import sys
import traceback
from collections import Counter

from pygments.formatters.html import HtmlFormatter
from werkzeug.exceptions import HTTPException

from main import *
from style import CustomMonokaiStyle
from . import *


@learning_bp.route('/pygments.css')
def pygments_css():
	style = HtmlFormatter(style=CustomMonokaiStyle).style
	return pygments_style_defs(style), 200, {'Content-Type': 'text/css'}


@learning_bp.errorhandler(Exception)
def handle_exception(e):
	if isinstance(e, HTTPException):
		return render_template("learning/404.html"), e.code


@learning_bp.route("/projects")
def projects():
	from projects import projects
	return render_template("learning/projects.html", description="All projects", projects=projects)


@learning_bp.route("/about")
def about():
	return render_template("learning/about.html")


@learning_bp.route("/")
def index():
	# app.config["FLATPAGES_ROOT"] = os.path.join(app.root_path, "posts")
	# flatpages.reload()
	app.logger.debug("flatpages_root = %s", app.config["FLATPAGES_ROOT"])
	app.logger.debug("flatpages = %s", [p.path for p in flatpages])
	try:
		_posts = get_all_posts(PREFIX)
		return render_template("learning/index.html", posts=_posts)
	except Exception:
		traceback.print_exc()


@learning_bp.route("/posts/<postname>")
def show_post(postname):
	try:
		post = flatpages.get_or_404(PREFIX + postname)
		return render_template("learning/post.html", post=post)
	except Exception:
		traceback.print_exc()


@learning_bp.route("/posts")
def posts():
	_posts = get_all_posts(PREFIX)
	return render_template("learning/posts.html", posts=_posts)


@learning_bp.route("/categories")
def categories():
	_posts = get_all_posts(PREFIX)
	categories_counter = Counter(p["category"] for p in _posts)
	return render_template(
		"learning/listing.html", metadata_type="categories", metadata_listing=sorted(categories_counter.items())
	)


@learning_bp.route("/categories/<name>")
def show_posts_with_category(name):
	_posts = get_all_posts(PREFIX)
	return render_template("learning/posts.html", posts=_posts, filter_category=name)


@learning_bp.route("/tags")
def tags():
	_posts = get_all_posts(PREFIX)
	tags_counter = Counter(tag for p in _posts for tag in p["tags"])
	return render_template(
		"learning/listing.html", metadata_type="tags", metadata_listing=sorted(tags_counter.items())
	)


@learning_bp.route("/tags/<name>")
def show_posts_with_tag(name):
	_posts = get_all_posts(PREFIX)
	return render_template("learning/posts.html", posts=_posts, filter_tag=name)


@learning_bp.route("/search", methods=["GET", "POST"])
def search():
	# from forms import SearchForm
	# search_form = SearchForm()

	if request.method == "GET":
		query = request.args.get("s")
		results = []
		_posts = get_all_posts(PREFIX)
		for post in _posts:
			# TODO: Elastic search
			if post["category"].find(query) != -1 or any(tag.find(query) != -1 for tag in post["tags"]) \
					or post["title"].find(query) != -1:
				results.append(post)

		results.sort(key=lambda item: (not item["pinned"], item["date"]))
		return render_template("learning/results.html", query=query, results=results)

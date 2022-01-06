import os
import sys
import traceback

from flask import *
from flask_flatpages import *
from pygments.formatters.html import HtmlFormatter
from werkzeug.exceptions import HTTPException

from main import *
from style import CustomMonokaiStyle

PREFIX = "learning/"
learning_bp = Blueprint(
	'learning', __name__,
	template_folder='./templates',
	static_folder='./static'
)


@learning_bp.route('/pygments.css')
def pygments_css():
	style = HtmlFormatter(style=CustomMonokaiStyle).style
	return pygments_style_defs(style), 200, {'Content-Type': 'text/css'}


@learning_bp.errorhandler(Exception)
def handle_exception(e):
	if isinstance(e, HTTPException):
		return render_template("404.html"), e.code


@learning_bp.route("/projects")
def projects():
	from projects import projects
	return render_template("projects.html", description="All projects", projects=projects)


@learning_bp.route("/about")
def about():
	return render_template("about.html")


@learning_bp.route("/")
def index():
	# app.config["FLATPAGES_ROOT"] = os.path.join(app.root_path, "posts")
	# flatpages.reload()
	app.logger.debug("flatpages_root = %s", app.config["FLATPAGES_ROOT"])
	app.logger.debug("flatpages = %s", [p.path for p in flatpages])
	try:
		_posts = get_all_posts(PREFIX)
		return render_template("index.html", posts=_posts)
	except Exception:
		traceback.print_exc()


@learning_bp.route("/posts/<postname>")
def show_post(postname):
	post = flatpages.get_or_404(PREFIX + postname)
	return render_template("post.html", post=post)


@learning_bp.route("/posts")
def posts():
	_posts = get_all_posts(PREFIX)
	return render_template("posts.html", posts=_posts)


@learning_bp.route("/categories")
def categories():
	_categories = {}
	for p in flatpages:
		category = p["category"]
		_categories[category] = _categories.get(category, 0) + 1

	return render_template("listing.html", metadata_type="categories", metadata_listing=sorted(_categories.items()))


@learning_bp.route("/categories/<name>")
def show_posts_with_category(name):
	_posts = get_all_posts(PREFIX)
	return render_template("posts.html", posts=_posts, filter_category=name)


@learning_bp.route("/tags")
def tags():
	_tags = {}
	for p in flatpages:
		for tag in p["tags"]:
			_tags[tag] = _tags.get(tag, 0) + 1

	return render_template("listing.html", metadata_type="tags", metadata_listing=sorted(_tags.items()))


@learning_bp.route("/tags/<name>")
def show_posts_with_tag(name):
	_posts = get_all_posts(PREFIX)
	return render_template("posts.html", posts=_posts, filter_tag=name)


@learning_bp.route("/search", methods=["GET", "POST"])
def search():
	# from forms import SearchForm
	# search_form = SearchForm()

	if request.method == "GET":
		query = request.args.get("s")
		results = []
		for post in list(flatpages):
			# TODO: Elastic search
			if post["category"].find(query) != -1 or any(tag.find(query) != -1 for tag in post["tags"]) \
					or post["title"].find(query) != -1:
				results.append(post)

		results.sort(key=lambda item: (not item["pinned"], item["date"]))
		return render_template("results.html", query=query, results=results)

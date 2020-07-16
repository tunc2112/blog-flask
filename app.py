from flask import *
from flask_flatpages import *
# from flask_frozen import Freezer
# from flaskext.markdown import Markdown
from pygments.formatters import HtmlFormatter
import sys
from werkzeug.exceptions import HTTPException

from config import *
from style import CustomMonokaiStyle

app = Flask(__name__)
app.config.from_object('config.SiteConfiguration')
app.route = prefix_route(app.route, SiteConfiguration.get_baseurl())
flatpages = FlatPages(app)
flatpages.init_app(app)
# Markdown(app)
# freezer = Freezer(app)


@app.context_processor
def set_global_variable():
	r = {"site_" + k: v for k, v in SiteConfiguration.site_variables.items()}
	# print(SiteConfiguration.get_site_variables(), r)
	return dict(**r, site=SiteConfiguration.site_variables)


@app.route('/pygments.css')
def pygments_css():
	style = HtmlFormatter(style=CustomMonokaiStyle).style
	return pygments_style_defs(style), 200, {'Content-Type': 'text/css'}


@app.route("/")
def index():
	_posts = [p for p in flatpages if p.path.startswith("")]
	_posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("index.html", posts=_posts)


@app.errorhandler(Exception)
def handle_exception(e):
	if isinstance(e, HTTPException):
		return render_template("404.html"), e.code


@app.route("/posts/<postname>")
def show_post(postname):
	post = flatpages.get_or_404(postname)
	return render_template("post.html", post=post)


@app.route("/posts")
def posts():
	_posts = list(flatpages)  # [p for p in flatpages if p.path.startswith("")]
	_posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", posts=_posts)


@app.route("/categories")
def categories():
	_categories = {}
	for p in flatpages:
		category = p["category"]
		_categories[category] = _categories.get(category, 0) + 1

	return render_template("listing.html", metadata_type="categories", metadata_listing=sorted(_categories.items()))


@app.route("/categories/<name>")
def show_posts_with_category(name):
	_posts = list(flatpages)  # [p for p in flatpages if p.path.startswith("")]
	_posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", posts=_posts, filter_category=name)


@app.route("/tags")
def tags():
	_tags = {}
	for p in flatpages:
		for tag in p["tags"]:
			_tags[tag] = _tags.get(tag, 0) + 1

	return render_template("listing.html", metadata_type="tags", metadata_listing=sorted(_tags.items()))


@app.route("/tags/<name>")
def show_posts_with_tag(name):
	_posts = list(flatpages)  # [p for p in flatpages if p.path.startswith("")]
	_posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", posts=_posts, filter_tag=name)


@app.route("/projects")
def projects():
	from projects import projects
	return render_template("projects.html", description="All projects", projects=projects)


@app.route("/about")
def about():
	return render_template("about.html")


@app.route("/search", methods=["GET", "POST"])
def search():
	# from forms import SearchForm
	# search_form = SearchForm()

	if request.method == "GET":
		query = request.args.get("s")
		results = []
		for post in list(flatpages):
			# TODO: Elastic search
			if post["category"].find(query) != -1 or any(tag.find(query) != -1 for tag in post["tags"])\
				or post["title"].find(query) != -1:
				results.append(post)

		results.sort(key=lambda item: (not item["pinned"], item["date"]))
		return render_template("results.html", query=query, results=results)


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		# freezer.freeze()
		pass
	else:
		app.run(host="localhost", port=5000, debug=True)

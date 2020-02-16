from flask import *
from flask_flatpages import *
# from flask_frozen import Freezer
# from flaskext.markdown import Markdown
from pygments.formatters import HtmlFormatter
import sys

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
	r = {"site_" + k: v for k, v in SiteConfiguration.get_site_variables().items()}
	# print(SiteConfiguration.get_site_variables(), r)
	return r


@app.route('/pygments.css')
def pygments_css():
	style = HtmlFormatter(style=CustomMonokaiStyle).style
	return pygments_style_defs(style), 200, {'Content-Type': 'text/css'}


@app.route("/")
def index():
	posts = [p for p in flatpages if p.path.startswith("")]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("index.html", posts=posts)


@app.errorhandler(404)
def page_not_found(e):
	# print(e)
	return render_template("404.html"), 404


@app.route("/posts/<postname>")
def show_post(postname):
	post = flatpages.get_or_404(postname)
	return render_template("post.html", post=post)


@app.route("/posts")
def posts():
	posts = list(flatpages)  # [p for p in flatpages if p.path.startswith("")]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", posts=posts)


@app.route("/categories")
def categories():
	categories = {}
	for p in flatpages:
		category = p["category"]
		categories[category] = categories.get(category, 0) + 1

	return render_template("listing.html", metadata_type="categories", metadata_listing=sorted(categories.items()))


@app.route("/categories/<name>")
def show_posts_with_category(name):
	posts = list(flatpages)  # [p for p in flatpages if p.path.startswith("")]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", posts=posts, filter_category=name)


@app.route("/tags")
def tags():
	tags = {}
	for p in flatpages:
		for tag in p["tags"]:
			tags[tag] = tags.get(tag, 0) + 1

	return render_template("listing.html", metadata_type="tags", metadata_listing=sorted(tags.items()))


@app.route("/tags/<name>")
def show_posts_with_tag(name):
	posts = list(flatpages)  # [p for p in flatpages if p.path.startswith("")]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", posts=posts, filter_tag=name)


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

from flask import *
from flask_flatpages import *
# from flask_frozen import Freezer
# from flaskext.markdown import Markdown
import sys

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"
FLATPAGES_ROOT = "posts"
FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite"]

app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)
flatpages.init_app(app)
# Markdown(app)
# freezer = Freezer(app)


@app.route("/")
def welcome():
	posts = [p for p in flatpages if p.path.startswith("")]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("index.html", posts=posts)


@app.errorhandler(404)
def page_not_found(e):
	# print(e)
	return render_template("404.html"), 404


@app.route("/posts")
def show_posts():
	posts = [p for p in flatpages if p.path.startswith("")]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", description="", posts=posts)


@app.route("/posts/<postname>")
def show_post(postname):
	post = flatpages.get_or_404(postname)
	return render_template("post.html", post=post)


@app.route("/tags")
def show_tags():
	tags = {}
	for p in flatpages:
		for tag in p["tags"]:
			tags[tag] = tags.get(tag, 0) + 1

	return render_template("tags.html", tags=sorted(tags.items()))


@app.route("/tags/<tagname>")
def show_posts_with_tags(tagname):
	posts = [p for p in flatpages if tagname in p["tags"]]
	posts.sort(key=lambda item: (not item["pinned"], item["date"]))
	return render_template("posts.html", description="All posts with tag #" + tagname, posts=posts)


@app.route("/projects")
def show_projects():
	projects = [{"name": "blog-flask", "description": "Blog written in Flask"}]
	return render_template("projects.html", description="All projects", projects=projects)


@app.route("/about")
def about():
	return render_template("about.html")


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		# freezer.freeze()
		pass
	else:
		app.run(host="localhost", port=5000, debug=True)

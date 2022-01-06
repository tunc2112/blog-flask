import sys

from flask import *
from flask_flatpages import *
# from flask_frozen import Freezer
# from flaskext.markdown import Markdown
from pygments.formatters.html import HtmlFormatter
from werkzeug.exceptions import HTTPException

from main import app
from config import *
from style import CustomMonokaiStyle

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		# freezer.freeze()
		pass
	else:
		app.run(host="localhost", port=5000, debug=True)

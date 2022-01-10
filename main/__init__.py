from datetime import datetime

from flask import *
from flask_flatpages import *

from config import *

app = Flask(__name__)
app.config.from_object('config.SiteConfiguration')
app.route = prefix_route(app.route, SiteConfiguration.get_baseurl())
flatpages = FlatPages(app)


def get_all_posts(prefix=""):
	return sorted(
		[p for p in flatpages if p.path.startswith(prefix)],
		key=lambda item: (not item["pinned"], item["date"])
	)


@app.context_processor
def set_global_variable():
	r = {"site_" + k: v for k, v in SiteConfiguration.site_variables.items()}
	# print(SiteConfiguration.get_site_variables(), r)
	return dict(**r, site=SiteConfiguration.site_variables, site_now=datetime.now())


# app.logger.debug("url_map = %s", app.url_map)
app.logger.debug("prefix = %s", app.root_path)
app.logger.debug("flatpages_root = %s", app.config["FLATPAGES_ROOT"])
app.logger.debug("flatpages = %s", [p.path for p in flatpages])

import main.views

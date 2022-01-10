from flask import Blueprint

PREFIX = "blog/"
blog_bp = Blueprint(
	'blog', __name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/blog'
)

import blog.views

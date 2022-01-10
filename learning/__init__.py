from flask import Blueprint

PREFIX = "learning/"
learning_bp = Blueprint(
	'learning', __name__,
	template_folder='templates',
	static_folder='static',
	url_prefix='/learning'
)

import learning.views

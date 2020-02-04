from pygments.styles.monokai import MonokaiStyle
from pygments.token import *


class CustomMonokaiStyle(MonokaiStyle):
	default_style = "monokai"
	styles = MonokaiStyle.styles
	styles.update({
		Name.Builtin: "#66d9ef",  # range, print,...
		Name.Builtin.Pseudo: "#fd971f",  # self
	})

	# self: Name.Builtin.Pseudo:
	# https://github.com/pygments/pygments/blob/3f403687036fce8c9f3d49a5bb2a8bbcdc41c8ba/pygments/lexers/python.py#L124

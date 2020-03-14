import yaml


def load_from_yaml(file):
	with open(file, "r") as fi:
		content = yaml.load(fi, Loader=yaml.FullLoader)
		return content


class SiteObject(object):
	def __init__(self, d):
		if isinstance(d, dict):
			self.__dict__ = d


class SiteConfiguration:
	DEBUG = True
	FLATPAGES_AUTO_RELOAD = DEBUG
	FLATPAGES_EXTENSION = ".md"
	FLATPAGES_ROOT = "posts"
	FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite", "fenced_code", "tables"]

	site_variables = load_from_yaml("_config.yml")
	# BASEURL = __config_yml.get("baseurl", "/")

	@staticmethod
	def get_baseurl():
		return SiteConfiguration.site_variables.get("baseurl", "/")


def prefix_route(route_function, prefix='', mask='{0}{1}'):
	'''
	src from https://stackoverflow.com/a/37878456

	Defines a new route function with a prefix.
	The mask argument is a `format string` formatted with, in that order:
	  prefix, route
	'''
	def newroute(route, *args, **kwargs):
		'''New function to prefix the route'''
		return route_function(mask.format(prefix, route), *args, **kwargs)

	return newroute

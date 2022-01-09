import sys

from main import app

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		# freezer.freeze()
		pass
	else:
		app.run(host="localhost", port=5000, debug=True)

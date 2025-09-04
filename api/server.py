import sys

sys.path.append("../../pip-package/flask")

from flask import Flask
from post import post_bp

server = Flask(__name__)
server.register_blueprint(post_bp)

if __name__ == "__main__":
	server.run(debug=True,port=8080)
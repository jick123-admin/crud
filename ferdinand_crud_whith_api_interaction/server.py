import sys

sys.path.append("../pip-package/flask")

from flask import Flask
from home import home_bp

server = Flask(__name__)
server.register_blueprint(home_bp)

if __name__ == "__main__":
	server.run(debug=True,port=9090)
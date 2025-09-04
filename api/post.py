import sys

sys.path.append("../../pip-package/flask")

from flask import Blueprint, jsonify

post_bp = Blueprint("post",__name__)

@post_bp.route("/")
def post():
	student = [
		{"id":1, "name":"ferdinand", "age":32, "gender":"male"},
		{"id":2, "name":"muana", "age":34, "gender":"female"},
		{"id":3, "name":"mua", "age":4, "gender":"male"}
	]

	return jsonify(student)
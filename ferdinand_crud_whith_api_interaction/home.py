import sys

sys.path.append("../pip-package/flask")
sys.path.append("../pip-package/requests")

from flask import Blueprint, render_template, request, redirect
from config import get_db_connection

import requests


home_bp = Blueprint("home",__name__)

@home_bp.route("/")
def home():
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("select *from students")
	students = cursor.fetchall()
	conn.close()

	results = requests.get("http://127.0.0.1:8080/")
	data = results.json()

	return render_template("home.html", students=students, data=data)


@home_bp.route("/add", methods=["POST"])
def add():
	name = request.form["name"]
	age = request.form["age"]
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("insert into students(name,age) values(%s,%s)",(name,age))
	conn.commit()
	conn.close()
	return redirect("/")


@home_bp.route("/edit/<int:id>")
def edit(id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("select *from students where id=%s",(id,))
	student = cursor.fetchone()

	cursor.execute("select *from students")
	students = cursor.fetchall()

	conn.close()
	return render_template("home.html", student=student, students=students)

@home_bp.route("/update/<int:id>", methods=["POST"])
def update(id):
	name = request.form["name"]
	age = request.form["age"]
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("update students set name=%s, age=%s where id=%s",(name,age,id))
	conn.commit()
	conn.close()
	return redirect("/")

@home_bp.route("/delete/<int:id>")
def delete(id):
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("delete from students where id=%s",(id,))
	conn.commit()
	conn.close()
	return redirect("/")

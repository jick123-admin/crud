import sys

sys.path.append("../pip-package/pymysql")

import pymysql

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "ferdinand"

def get_db_connection():
	return pymysql.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,database=DB_NAME,cursorclass=pymysql.cursors.DictCursor)
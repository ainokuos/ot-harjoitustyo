import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname))
connection.row_factory = sqlite.Row

def get_database_connection():
	return connection

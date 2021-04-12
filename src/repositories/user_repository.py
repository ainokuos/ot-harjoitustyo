from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
	return User(row["username"], row["password"]) if row else None

def get_user_by_row(row):
	def __init__(self, connection):
		self._connection = connection

	def create(self, user):
		cursor = self._connetion.cursor()

		cursor.execute(" insert into uresrs (username, password) values (?, ?)", (user.username, user.password)) 

		self._connection.commit()

		return user

	def find_by_username(self, username):
		cursor = self._connection.cursor()

		cursor.execute(" select * from users where username = ?", (username, ))

		row = cuorsor.fetchone()

		return get_user_by_row(row)

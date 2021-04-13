import unittest
from initialize_database import initialize_database
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
	def setUp(self):
		initialize_database()
		self.user_timo = User("timo", "1234")

	def test_create(self):
		user_repository.create(self.user_timo)
		users = user_repository.find_all()

		self.assertEqual(len(users), 1)


from entities.user import User
from repositories.user_repository import user_repository



class TrackerService:

	def __init__(self):

		self.user = None
		self._user_repository = user_repository

	def login(self, username, password):

		user = self._user_repository.find_by_username(username)

		self._user = user

		return user

	def logout(self):
		self._user = None

	def get_users(self):
		return self._user_repository.find_all()

	def create_user(self, username, password):
		existing_user = self._user_repository.find_by_username(username)


		user = self._user_repository.create(User(username, password))


		return user

tracker_service = TrackerService()

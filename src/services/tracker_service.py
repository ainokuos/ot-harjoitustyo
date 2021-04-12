from entities.user import User


class TrackerService:

	def __init__(self, user_repository):

		self.user = None
		self._user_repository = user_repository

	def login(self, username, password):

		user = self._user_reposiroty.find_by_username(username)

		if not user or user.password != password:
			raise InvalidCredentialsError("Invalid username or password")

		self._user = user

		return user

	def logout(self):
		self._user = None

	def create_user(self, username, password, login = True):
		existing_user = self._user_repository.find_by_username(username)

		if existind_user:
			raise UsernameExistError(f"Username {username} already exists")

		user = self._user_repository.create(User(username, password))

		if login:
			self._user = user

		return user

from entities.user import User
from entities.note import Note
from repositories.user_repository import user_repository
from repositories.note_repository import note_repository



class TrackerService:

    def __init__(self):
        self.user = None
        self._user_repository = user_repository

    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            return False

        self.user = user

        return True

    def logout(self):
        self.user = None

    def get_users(self):
        return self._user_repository.find_all()

    def create_user(self, username, password):
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            return False

        user = self._user_repository.create(User(username, password))

        return True

    def create_note(self, name, cr, grade):
        note = Note(name, cr, grade, self.user.username)
        note_repository.create(note)
    
    def get_notes(self):
        return note_repository.find_all()
    
    def delete_notes(self):
        note_repository.delete_all()
        
tracker_service = TrackerService()

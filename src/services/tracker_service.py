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
        self._user_repository.create(User(username, password))

        return True

    def create_note(self, name, cr, grade):
        note = Note(name, cr, grade, self.user.username)
        note_repository.create(note)
    
    def get_notes(self):
        notes = note_repository.find_all()
        return [note for note in notes if note.username == self.user.username]

    def get_sum(self):
        notes = self.get_notes()
        points = 0
        for note in notes:
            if note.username == self.user.username:
                points += int(note.cr)
        return points
    
    def get_average(self):
        notes = self.get_notes()
        grades = 0
        total = 0
        for note in notes:
            if note.username == self.user.username:
                grades += int(note.grade)
                total +=1
        if total > 0:
            return f"{(grades/total):.2F}"
        return 0
    
    def delete_note(self, note):
        note_repository.delete_one(note)
        
    def delete_notes(self):
        note_repository.delete_all()
        
tracker_service = TrackerService()

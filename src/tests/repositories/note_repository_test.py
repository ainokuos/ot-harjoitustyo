import unittest
from repositories.note_repository import note_repository
from entities.note import Note
from entities.user import User

class TestNoteRepository(unittest.TestCase):
    def setUp(self):
        note_repository.delete_all()

        self.note = Note("tentti", "testi", "timo")
        self.note2 = Note("palautus", "testi2", "timo")
    
    def test_create_note(self):
        note_repository.create(self.note)
        notes = note_repository.find_all()
        self.assertEqual(len(notes), 1)
    
    def test_delete_note(self):
        note_repository.create(self.note)
        note_repository.create(self.note2)
        note_repository.delete_one(self.note)
        notes = note_repository.find_all()
        self.assertEqual(len(notes), 1)

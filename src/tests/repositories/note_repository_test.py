import unittest
from repositories.note_repository import note_repository
from entities.note import Note
from entities.user import User


class TestNoteRepository(unittest.TestCase):
    def setUp(self):
        note_repository.delete_all()

        self.user = User("timo", "123")
        self.note = Note("testi", 1, 1, "timo")
        self.note2 = Note("testi2", 2, 2, "timo")
    
    def test_create(self):
        note_repository.create(self.note)
        notes = note_repository.find_all()

        self.assertEqual(len(notes), 1)
    

    def test_delete_all(self):
        note_repository.create(self.note)
        note_repository.delete_all()
        notes = note_repository.find_all()
        
        self.assertEqual(len(notes), 0)
    
    def test_delete_one(self):
        note_repository.create(self.note)
        note_repository.create(self.note2)
        note_repository.delete_one(self.note2)
        notes = note_repository.find_all()

        self.assertEqual(len(notes),1)

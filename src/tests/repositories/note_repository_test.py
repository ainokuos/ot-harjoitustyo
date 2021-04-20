import unittest
from repositories.note_repository import note_repository
from entities.note import Note
from entities.user import User


class TestNoteRepository(unittest.TestCase):
    def setUp(self):
        note_repository.delete_all()

        self.user = User("timo", "123")
        self.note = Note("testi", 1, 1, "timo")
    
    def test_create(self):
        note_repository.create(self.note)
        notes = note_repository.find_all()

        self.assertEqual(len(notes), 1)


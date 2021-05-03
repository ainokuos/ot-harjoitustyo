import unittest
from entities.note import Note
from entities.user import User
from services.tracker_service import tracker_service

    
class TestTrackerService(unittest.TestCase):
    def setUp(self):
        self.tracker_service = tracker_service
        self.user = User("aino", "123")

    
    def test_create_user(self):
        user = self.user
        self.assertEqual(self.tracker_service.create_user(user.username, user.password), True)
        self.assertEqual(self.tracker_service.create_user(user.username, user.password), False)





    
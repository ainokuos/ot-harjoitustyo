import unittest
from entities.course import Course
from entities.user import User
from services.tracker_service import tracker_service

    
class TestTrackerService(unittest.TestCase):
    def setUp(self):
        self.tracker_service = tracker_service
        self.user = User("aino", "123")
        self.user2 = User("aino1", "000")

    def test_create_user(self):
        user = self.user
        self.assertEqual(self.tracker_service.create_user(user.username, user.password), True)
        self.assertEqual(self.tracker_service.create_user(user.username, user.password), False)

    def test_login(self):
        user = self.user2
        self.tracker_service.create_user(user.username, user.password)
        self.assertEqual((self.tracker_service.login("aino1", "000")), True)
        self.assertEqual((self.tracker_service.login("aino1", "123")), False)
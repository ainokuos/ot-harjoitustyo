import unittest
from repositories.course_repository import course_repository
from entities.course import Course
from entities.user import User


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all()

        self.user = User("timo", "123")
        self.course = Course("testi", 1, 1, "timo")
        self.course2 = Course("testi2", 2, 2, "timo")
    
    def test_create(self):
        course_repository.create(self.course)
        courses = course_repository.find_all()

        self.assertEqual(len(courses), 1)
    

    def test_delete_all(self):
        course_repository.create(self.course)
        course_repository.delete_all()
        courses = course_repository.find_all()
        
        self.assertEqual(len(courses), 0)
    
    def test_delete_one(self):
        course_repository.create(self.course)
        course_repository.create(self.course2)
        course_repository.delete_one(self.course2)
        courses = course_repository.find_all()

        self.assertEqual(len(courses),1)

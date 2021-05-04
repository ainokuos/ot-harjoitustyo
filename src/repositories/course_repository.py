from entities.course import Course
from config import COURSES_FILE_PATH
from repositories.csv_repository import CsvRepository

class CourseRepository:

    def __init__(self, file_path):
        self._file_path = file_path
        self.csv_repository = CsvRepository(self._file_path)

    def _read(self):
        courses = []
        self.csv_repository.ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                name = parts[0]
                cr = parts[1]
                grade = parts[2]
                username = parts[3]
                courses.append(Course(name,cr,grade, username))
            return courses

    def _write(self, courses):
        self.csv_repository.ensure_file_exists()
        with open(self._file_path, "w") as file:
            for course in courses:
                row = f"{course.name};{course.cr};{course.grade};{course.username}"
                file.write(row+"\n")

    def create(self, course):
        courses = self.find_all()
        courses.append(course)
        self._write(courses)
        return course 

    def find_all(self):
        return self._read()

    def delete_all(self):
        self.csv_repository.delete_all()

    def delete_one(self, course):
        courses = self.find_all()
        for i in courses:
            if course.name == i.name and course.username == i.username:
                courses.remove(i)
                self._write(courses)
                break
course_repository = CourseRepository(COURSES_FILE_PATH)

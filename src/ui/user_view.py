from tkinter import ttk, constants
from services.tracker_service import tracker_service

class UserView:

    def __init__ (self, root, handle_login, handle_add_course, handle_add_note):
        self._root = root
        self._handle_login = handle_login
        self._handle_add_course = handle_add_course
        self._handle_add_note = handle_add_note
        self._frame = None

        self._row = 5

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize_courses(self):
        courses = tracker_service.get_courses()
        for course in courses:
            self._initialize_course(course, self._row)
            self._row +=1

    def _initialize_notes(self):
        notes = tracker_service.get_notes()
        for note in notes:
            self._initialize_note(note, self._row)
            self._row +=1
    
    def _initialize_note(self, note, r):
        note_label = ttk.Label(master = self._frame, text = note.header)

        note_label.grid(row = r, column = 0)
        

    def _initialize_course(self, course, r):
        course_label = ttk.Label(master = self._frame, text = course.name)
        course_points = ttk.Label(master = self._frame, text = course.cr)
        course_grade = ttk.Label(master = self._frame, text = course.grade)

        course_label.grid(row = r, column = 0)
        course_points.grid(row = r, column = 1)
        course_grade.grid(row = r, column = 2)


    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Tervetuloa")

        add_course = ttk.Button(master = self._frame, text = "Lisää suoritus", command = self._handle_add_course)
        add_note = ttk.Button(master = self._frame, text = "Lisää muistiinpano", comman =self._handle_add_note)
        logout = ttk.Button(master = self._frame, text = "Kirjaudu ulos", command = self._handle_login)

        total = ttk.Label(master = self._frame, text = "Opintopisteet:" + str(tracker_service.get_sum()))
        average = ttk.Label(master = self._frame, text = f"Keskiarvo:{tracker_service.get_average()}")

        self._initialize_courses()
        self._initialize_notes()

        label.grid(row = 0, column = 1)
        add_course.grid(row = 1, column = 0)
        add_note.grid(row = 1, column = 1)
        logout.grid(row = 1, column = 3)
        total.grid(row = 2, column = 1)
        average.grid(row = 2, column = 2)
      




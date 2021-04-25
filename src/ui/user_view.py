from tkinter import ttk, constants
from services.tracker_service import tracker_service

class UserView:

    def __init__ (self, root, handle_login, handle_add):
        self._root = root
        self._handle_login = handle_login
        self._handle_add = handle_add
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_note(self, note, r):
        note_label = ttk.Label(master = self._frame, text = note.name)
        note_points = ttk.Label(master = self._frame, text = note.cr)
        note_grade = ttk.Label(master = self._frame, text = note.grade)

        note_label.grid(row = r, column = 0)
        note_points.grid(row = r, column = 1)
        note_grade.grid(row = r, column = 2)

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Tervetuloa")

        add = ttk.Button(master = self._frame, text = "Lisää suoritus", command = self._handle_add)

        logout = ttk.Button(master = self._frame, text = "Kirjaudu ulos", command = self._handle_login)
        notes = tracker_service.get_notes()
        r=5
        for note in notes:
            if note.username == tracker_service.user.username:
                self._initialize_note(note, r)
                r+=1

        label.grid(row = 0, column = 1)
        add.grid(row = 1, column = 1)
        logout.grid(row = 1, column = 3)
      




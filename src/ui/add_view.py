from tkinter import ttk, constants, StringVar
from services.tracker_service import tracker_service

class AddView:

    def __init__(self, root, handle_user):
        self._root = root
        self._handle_user = handle_user
        self._frame = None

        self._error_variable = None
        self._error_label = None

        self._name_entry = None
        self._credits_entry = None
        self._grade_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _add_note_handler(self):
        name = self._name_entry.get()
        credit = self._credits_entry.get()
        grade = self._grade_entry.get()

        try:
            int(credit)
            int(grade)
            tracker_service.create_note(name, credit, grade)
            self._handle_user()

        except ValueError:
            self._show_error("Anna opintopisteet ja arvosana numerona")
        
       
    def _initialize_add_fields(self):
        name_label = ttk.Label(master = self._frame, text = "Kurssin nimi")
        credits_label = ttk.Label(master = self._frame, text = "Opintopisteet")
        grade_label = ttk.Label(master = self._frame, text = "Arvosana")

        self._name_entry = ttk.Entry(master = self._frame)
        self._credits_entry = ttk.Entry(master = self._frame)
        self._grade_entry = ttk.Entry(master = self._frame)

        name_label.grid(row = 1, column = 0)
        self._name_entry.grid(row = 1, column = 1)

        credits_label.grid(row = 2, column = 0)
        self._credits_entry.grid(row = 2, column = 1)

        grade_label.grid(row = 3, column = 0)
        self._grade_entry.grid(row = 3, column = 1)
    
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Merkitse suoritus")

        goback_button = ttk.Button(master = self._frame, text = "Palaa", command = self._handle_user)
        add_button = ttk.Button(master = self._frame, text = "Lisää", command = self._add_note_handler)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master = self._frame, textvariable = self._error_variable)

        label.grid(row = 0, column = 0)
        goback_button.grid(row = 4, column = 0)
        add_button.grid(row = 4, column = 1)

        self._error_label.grid(row = 4, column = 2)

        self._initialize_add_fields()
        self._hide_error()


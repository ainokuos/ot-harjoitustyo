from tkinter import ttk, constants, StringVar
from services.tracker_service import tracker_service

class CreateView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None

        self._username_entry = None
        self._password_entry= None

        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Anna käyttäjätunnus ja salasana")

        else:

            if tracker_service.create_user(username, password) == True:
                self._handle_login()
            else:
                self._show_error(f"Käyttäjänimi {username} on jo käytössä")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_frames(self):
        username_label = ttk.Label(master = self._frame, text = "Käyttäjätunnus")
        self._username_entry = ttk.Entry(master = self._frame)

        password_label = ttk.Label(master = self._frame, text = "Salasana")
        self._password_entry = ttk.Entry(master = self._frame)

        username_label.grid(row = 1, column = 0)
        self._username_entry.grid(row = 1, column = 1)

        password_label.grid(row = 2, column = 0)
        self._password_entry.grid(row = 2, column = 1)

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)


        create = ttk.Button(master = self._frame, text = "Luo", command = self._create_user_handler)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master = self._frame, textvariable = self._error_variable)


        create.grid(row = 3, column = 0)

        self._error_label.grid(row = 4, column = 0)

        self._initialize_frames()

        self._hide_error()



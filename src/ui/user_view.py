from tkinter import ttk, constants

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

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Tervetuloa")

        add = ttk.Button(master = self._frame, text = "Lisää suoritus", command = self._handle_add)

        logout = ttk.Button(master = self._frame, text = "Kirjaudu ulos", command = self._handle_login)

        label.grid(row = 0, column = 1)
        add.grid(row = 1, column = 1)
        logout.grid(row = 2, column = 1)



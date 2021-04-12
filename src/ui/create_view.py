from tkinter import ttk, constants

class CreateView:
	def __init__(self, root, handle_login):
		self._root = root
		self._handle_login = handle_login
		self._frame = None

		self._initialize()

	def pack(self):
		self._frame.pack(fill = constants.X)

	def destroy(self):
		self._frame.destroy()

	def _initialize(self):
		self._frame = ttk.Frame(master = self._root)

		username_label = ttk.Label(master = self._frame, text = "Käyttäjätunnus")
		username_entry = ttk.Entry(master = self._frame)

		password_label = ttk.Label(master = self._frame, text = "Salasana")
		password_entry = ttk.Entry(master = self._frame)

		create = ttk.Button(master = self._frame, text = "Luo", command = self._handle_login)

		username_label.grid(row = 1, column = 0)
		username_entry.grid(row = 1, column = 1)

		password_label.grid(row = 2, column = 0)
		password_entry.grid(row = 2, column = 1)

		create.grid(row = 3, column = 0)


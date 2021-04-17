from tkinter import ttk, constants

class AddView:

    def __init__(self, root, handle_user):
        self._root = root
        self._handle_user = handle_user
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill = constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Merkitse suoritus")

        goback = ttk.Button(master = self._frame, text = "Palaa", command = self._handle_user)

        label.grid(row = 0, column = 0)
        goback.grid(row = 1, column = 0)


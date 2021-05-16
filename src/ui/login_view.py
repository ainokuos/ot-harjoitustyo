from tkinter import  ttk, constants, StringVar
from services.tracker_service import tracker_service

class LoginView:
    """ Luokka, joka vastaa kirjautumisnäkymästä

        Attributes:
            root: juurikomponentti
            handle_user: kutsu tervetuloa-näkymään
            handle_create: kutsu käyttäjän luomisen näkymään
    """
    def __init__ (self, root, handle_user, handle_create):
        """ Luokan konstruktori, joka luo uuden kirjautumisnäkymän. 

            Args:
                root: juurikomponentti
                handle_user: kutsu tervetuloa-näkymään
                handle_create: kutsu käyttäjän luomisen näkymään
        """
        self._root = root
        self._handle_user = handle_user
        self._handle_create = handle_create
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """ Asettelee näkymän """
        self._frame.pack(fill = constants.X)

    def destroy(self):
        """ Piilottaa näkymän """
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()


        if tracker_service.login(username, password) == True:
            self._handle_user()

        else:
            self._show_error(f"Virheellinen käyttäjänimi tai salasana")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()


    def _initialize_fields(self):
        username_label = ttk.Label(master = self._frame, text = "Käyttäjätunnus")
        password_label = ttk.Label(master = self._frame, text = "Salasana")

        self._username_entry = ttk.Entry(master = self._frame)
        self._password_entry = ttk.Entry(master = self._frame)

        username_label.grid(row = 1, column = 0)
        self._username_entry.grid(row = 1, column = 1)

        password_label.grid(row = 2, column = 0)
        self._password_entry.grid(row = 2, column = 1)

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Kirjaudu sisään", font = ("Arial", 16))

        self._initialize_fields()

        login_button = ttk.Button(master = self._frame, text = "Kirjaudu", command = self._login_handler)

        create = ttk.Button(master = self._frame, text = "Luo tunnus", command = self._handle_create)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master = self._frame, textvariable = self._error_variable, foreground = "red")

        label.grid(row = 0, column = 0)


        login_button.grid(row = 3, column = 0, pady = 3)
        create.grid(row = 3, column = 1, pady = 3)

        self._hide_error()

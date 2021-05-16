from tkinter import ttk, constants, StringVar
from services.tracker_service import tracker_service
class AddNoteView:
    """ Luokka, joka vastaa muistiinpanon lisäämisen näkymästä.

        Attributes:
            root: juurikomponentti
            handle_user: kutsu tervetuloa-näkymään
    """
    def __init__(self, root, handle_user):
        """ Luokan konstruktori, joka luo uuden muistiinpanonäkymän.

            Args:
                root: juurikomponentti
                handle_user: kutsu tervetuloa-näkymään
        """
        self._root = root
        self._handle_user = handle_user
        self._frame = None

        self._error_variable = None
        self._error_label = None 

        self._var = StringVar()
        self._message_entry = None 

        self._initialize()

    def pack(self):
        """ Asettelee näkymän. """
        self._frame.pack(fill = constants.X)

    def destroy(self):
        """ Piilottaa näkymän. """
        self._frame.destroy()
    
    def _add_note_handler(self):
        header = str(self._var.get())
        message = self._message_entry.get()

        if len(header) == 0 or len(message) == 0:
            self._show_error("Tietoja puuttuu")
        else:

            tracker_service.create_note(header, message)

            self._handle_user()
    
    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()
    
    def _handle_delete(self, note):
        tracker_service.delete_note(note)
        self._handle_user()
    
    def _initialize_notes(self):
        notes = tracker_service.get_notes()
        r = 6
        for note in notes:
            self._initialize_note(note, r)
            r += 1
    
    def _initialize_note(self, note, r):
        note_header = ttk.Label(master = self._frame, text = note.header)
        note_message = ttk.Label(master = self._frame, text = note.message)
        note_delete = ttk.Button(master = self._frame, text = "Poista", command = lambda: self._handle_delete(note))
    
        note_header.grid(row = r, column = 0)
        note_message.grid(row = r, column = 1)
        note_delete.grid(row = r, column = 3, pady = 3)
    
    def _initialize_add_fields(self):
        header1 = ttk.Radiobutton(master = self._frame, text = "Tentti",variable = self._var,value = "Tentti")
        header2 = ttk.Radiobutton(master = self._frame, text = "Palautus", variable = self._var, value = "Palautus")
        header3 = ttk.Radiobutton(master = self._frame, text = "Ilmottautuminen", variable = self._var, value = "Ilmottautuminen")
        self._message_entry = ttk.Entry(master = self._frame)
        

        header1.grid(row = 1, column = 0, sticky = (constants.W, constants.E))
        header2.grid(row = 1, column = 1, sticky = (constants.W, constants.E))
        header3.grid(row = 1, column = 2, sticky = (constants.W, constants.E))

        self._message_entry.grid(row = 2, column = 0, columnspan = 3)

        

    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Lisää muistiinpano", font = ("Arial", 16))

        add_button = ttk.Button(master = self._frame, text = "Lisää", command = self._add_note_handler)
        return_button = ttk.Button(master = self._frame, text = "Palaa", command = self._handle_user)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master = self._frame, textvariable = self._error_variable, foreground = "red")

        label.grid(row = 0, column = 0, columnspan = 3)
        add_button.grid(row = 4, column = 0, sticky = constants.W, pady = 5)
        return_button.grid(row = 0, column = 3)

        self._error_label.grid(row = 5, column = 0)

        self._initialize_add_fields()
        self._initialize_notes()
        self._hide_error()
        
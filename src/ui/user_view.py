from tkinter import ttk, constants
from services.tracker_service import tracker_service

class UserView:
    """ Luokka, joka vastaa tervetuloa-näkymästä

        Attributes:
            root: juurikomponentti
            handle_login: kutsu kirjautumisnäkymään
            handle_add_course: kutsu suorituksenlisäys näkymään
            handle_add_note: kutsu muistiinpanon lisäämisen näkymään
    """
    def __init__ (self, root, handle_login, handle_add_course, handle_add_note):
        """ Luokan kjonstruktori, joka luo uuden tervetuloa-näkymän

            Args:
                root: juurikomponentti
                handle_login: kutsu kirjautumisenäkymään
                handle_add_course: kutsu kurssin lisäämisen näkymään
                handle_add_note: kutsu muistiinpanon lisäämisen näkymään
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_add_course = handle_add_course
        self._handle_add_note = handle_add_note
        self._frame = None

        self._row = 7

        self._initialize()

    def pack(self):
        """ Asettelee näkymän """
        self._frame.pack(fill = constants.X)

    def destroy(self):
        """ Piilottaa näkymän """
        self._frame.destroy()
    
    def _initialize_courses(self):
        columns = ('#1', '#2', '#3')
        tree = ttk.Treeview(master = self._frame,height = 2 ,columns = columns, show = 'headings')
        tree.heading('#1', text = "Kurssi")
        tree.heading('#2', text = "Opintopisteet")
        tree.heading('#3', text = "Arvosana")

        contacts = []

        courses = tracker_service.get_courses()
        for course in courses:
            contacts.append((f'{course.name}', f'{course.cr}', f'{course.grade}'))
            
        for contact in contacts:
            tree.insert('','end', values = contact)
        
        scrollbar = ttk.Scrollbar(self._frame, orient = 'vertical', command = tree.yview)
        tree.configure(yscroll = scrollbar.set)
        scrollbar.grid(row = 5 ,column = 3, sticky = (constants.S, constants.N, constants.W))
        
        tree.grid(row = 5, column = 0, sticky = (constants.S, constants.N), columnspan = 3)

    def _initialize_notes(self):
        notes = tracker_service.get_notes()
        notes_label = ttk.Label(master = self._frame, text = "Muistio", font = ("Arial", 12))
        notes_label.grid(row = self._row, column = 0, pady = 5)
        for note in notes:
            self._row +=1
            self._initialize_note(note, self._row)
    
    def _initialize_note(self, note, r):
        note_label = ttk.Label(master = self._frame, text = note.header)
        note_message = ttk.Label(master = self._frame, text = note.message)

        note_label.grid(row = r, column = 0)
        note_message.grid(row = r, column = 1)
        
    def _initialize(self):
        self._frame = ttk.Frame(master = self._root)
        label = ttk.Label(master = self._frame, text = "Tervetuloa", font = ("Arial", 16))

        add_course = ttk.Button(master = self._frame, text = "Lisää suoritus", command = self._handle_add_course)
        add_note = ttk.Button(master = self._frame, text = "Lisää muistiinpano", comman =self._handle_add_note)
        logout = ttk.Button(master = self._frame, text = "Kirjaudu ulos", command = self._handle_login)

        total = ttk.Label(master = self._frame, text = "Opintopisteet:" + str(tracker_service.get_sum()), font = ("Arial", 12))
        average = ttk.Label(master = self._frame, text = f"Keskiarvo:{tracker_service.get_average()}", font = ("Arial", 12))

        self._initialize_courses()
        self._initialize_notes()

        label.grid(row = 0, column = 0, padx = 10)
        add_course.grid(row = 2, column = 0)
        add_note.grid(row = 7, column = 1)
        logout.grid(row = 0, column = 3)
        total.grid(row = 2, column = 1)
        average.grid(row = 2, column = 2)
      




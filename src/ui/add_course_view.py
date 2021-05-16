from tkinter import ttk, constants, StringVar
from services.tracker_service import tracker_service

class AddCourseView:
    """ Luokka, joka vastaa kurssinlisäysnäkymästä.

        Attributes:
            root: juurikomponentti
            handle_user: kutsu tervetuloa-näkymään
    """

    def __init__(self, root, handle_user):
        """ Luokan konstruktori, joka luo uuden kurssinlisäysnäkymän.

            Args.
                root: juurikomponentti
                handle_user: kutsu tervetuloa-näkymään
        """
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
        """ Asettelee näkymän. """
        self._frame.pack(fill = constants.X)

    def destroy(self):
        """ Piilottaa näkymän. """
        self._frame.destroy()
    
    def _add_course_handler(self):
        name = self._name_entry.get()
        credit = self._credits_entry.get()
        grade = self._grade_entry.get()

        try:
            if int(credit) <=0 or int(grade)<=0:
                self._show_error("Anna opintopisteet ja arvosana")
            if int(grade)>5:
                self._show_error("Anna arvosana väliltä 1-5")
            elif int(credit)>0 and 0<int(grade)<=5:
                tracker_service.create_course(name, credit, grade)
                self._handle_user()

        except ValueError:
            self._show_error("Anna opintopisteet ja arvosana numerona")
    
    def _initialize_courses(self):
        courses = tracker_service.get_courses()
        r = 5
        for course in courses:
            self._initialize_course(course, r)
            r += 1
    
    def _initialize_course(self,course, r):
        course_name = ttk.Label(master = self._frame, text = course.name)
        course_delete = ttk.Button(master = self._frame, text = "Poista", command = lambda: self._handle_delete(course))

        course_name.grid(row = r, column = 0)
        course_delete.grid(row = r, column = 3, pady = 3)
    
    def _handle_delete(self, course):
        tracker_service.delete_course(course)
        self._handle_user()

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
        label = ttk.Label(master = self._frame, text = "Merkitse suoritus", font = ("Arial", 16))

        goback_button = ttk.Button(master = self._frame, text = "Palaa", command = self._handle_user)
        add_button = ttk.Button(master = self._frame, text = "Lisää", command = self._add_course_handler)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master = self._frame, textvariable = self._error_variable, foreground = "red")

        label.grid(row = 0, column = 0)
        goback_button.grid(row = 0, column = 3)
        add_button.grid(row = 4, column = 0)

        self._error_label.grid(row = 4, column = 2)

        self._initialize_add_fields()
        self._initialize_courses()
        self._hide_error()


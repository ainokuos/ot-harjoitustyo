from ui.login_view import LoginView
from ui.user_view import UserView
from ui.add_course_view import AddCourseView
from ui.add_note_view import AddNoteView
from ui.create_view import CreateView

class UI:
    """ Luokka, joka vastaa käyttöliittymästä

        Attributes:
            root: juurikomponentti
    """
    def __init__(self, root):
        """ Luokan konstruktori, joka luo uuden näkymän

            Args:
                root: juurikomponentti
        """
        self._root = root
        self._current_view = None

    def start(self):
        """ Näyttää aloitusnäkymän. """       
        self._show_login_view()


    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_user(self):
        self._show_user_view()

    def _handle_login(self):
        self._show_login_view()

    def _handle_add_course(self):
        self._show_add_course_view()

    def _handle_add_note(self):
        self._show_add_note_view()

    def _handle_create(self):
        self._show_create_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view=LoginView(self._root, self._handle_user, self._handle_create)

        self._current_view.pack()

    def _show_user_view(self):
        self._hide_current_view()

        self._current_view=UserView(self._root, self._handle_login, self._handle_add_course, self._handle_add_note)

        self._current_view.pack()

    def _show_add_course_view(self):
        self._hide_current_view()

        self._current_view=AddCourseView(self._root, self._handle_user)

        self._current_view.pack()
    
    def _show_add_note_view(self):
        self._hide_current_view()

        self._current_view=AddNoteView(self._root, self._handle_user)

        self._current_view.pack()

    def _show_create_view(self):
        self._hide_current_view()

        self._current_view=CreateView(self._root, self._handle_login)

        self._current_view.pack()

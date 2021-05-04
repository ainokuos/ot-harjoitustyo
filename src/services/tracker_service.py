from entities.user import User
from entities.course import Course
from entities.note import Note
from repositories.user_repository import user_repository
from repositories.course_repository import course_repository
from repositories.note_repository import note_repository


class TrackerService:
    """ Luokka, joka vastaa sovelluslogiikasta. """

    def __init__(self):
        """ Luokan konstruktori, joka luo palvelun yksittäiselle käyttäjälle. """
        self.user = None

    def login(self, username, password):
        """ Kirjaa käyttäjän sisään.

        Args:
            username: käyttäjän tunnus
            password: käyttäjän salasana
        Returns:
            True, jos käyttäjänimi ja salasana täsmäävät
            False, jos käyttäjänimi ja salasana eivät täsmää tai käyttäjää ei löydy
        """
        user = user_repository.find_by_username(username)

        if not user or user.password != password:
            return False

        self.user = user

        return True

    def logout(self):
        """ Kirjaa käyttäjän ulos. """
        self.user = None

    def get_users(self):
        """ Hakee kaikki käyttäjät.

            Returns:
                User-olioita sisältävän listan käyttäjistä
        """
        return user_repository.find_all()

    def create_user(self, username, password):
        """ Luo uuden käyttäjän.

            Args:
                username: Merkkijono, joka kuvaa käyttäjän tunnusta
                password: Merkkijono, joka kuvaa käyttäjän salasanaa
            Returns:
                True, jos käyttäjää ei ole olemassa
                False, jos käyttäjänimi on jo käytössä tai salasana puuttuu
        """
        existing_user = user_repository.find_by_username(username)

        if existing_user:
            return False
        user_repository.create(User(username, password))

        return True

    def create_course(self, name, cr, grade):
        """ Luo uuden suorituksen.

        Args:
            name: Merkkijono, joka kuvaa suorituksen nimeä
            cr: Numeroarvo, joka kuvaa suorituksen opintopisteitä
            grade: Numeroarvo, jok kuvaa suorituksen arvosanaa
        """
        course = Course(name, cr, grade, self.user.username)
        course_repository.create(course)

    def get_courses(self):
        """ Hakee kaikki suoritukset.

            Returns:
                Lista kirjautuneen käyttäjän suorituksista
        """
        courses = course_repository.find_all()
        return [course for course in courses if course.username == self.user.username]

    def get_sum(self):
        """ Laskee opintopisteiden summan.

            Returns:
                Opintopisteiden summan
        """
        courses = self.get_courses()
        points = 0
        for course in courses:
            if course.username == self.user.username:
                points += int(course.cr)
        return points

    def get_average(self):
        """ Laskee arvosanojen keskiarvon.

            Returns:
                Arvosanojen keskiarvon pyöristettynä
                0 , jos suorituksia ei ole
        """
        courses = self.get_courses()
        grades = 0
        total = 0
        for course in courses:
            if course.username == self.user.username:
                grades += int(course.grade)
                total +=1
        if total > 0:
            return f"{(grades/total):.2F}"
        return 0

    def delete_course(self, course):
        """ Poistaa yksittäisen suorituksen.

            Args:
                note: Poistettava suoritus Note-oliona
        """
        course_repository.delete_one(course)

    def delete_courses(self):
        """ Poistaa kaikki suoritukset. """
        course_repository.delete_all()

    def create_note(self, header, message):
        """ Luo uuden muistiinapnon.

            Args:
                header: Merkkijono, joka kuvaa muistiinpanon otsikkoa
                message: Merkkijono, joka kuvaa muistiinpanon sisältöä
        """
        note = Note(header, message, self.user.username)
        note_repository.create(note)

    def get_notes(self):
        """ Hakee kaikki muistiinpanot.

            Returns:
                kaikki käyttäjän lisäämät muistiinpanot listana
        """
        notes = note_repository.find_all()
        return [note for note in notes if note.username == self.user.username]

    def delete_notes(self):
        """ Poistaa kaikki muistiinpanot. """
        note_repository.delete_all()
    
    def delete_note(self, note):
        """ Poistaa yksittäisen muistiinpanon. """
        note_repository.delete_one(note)

tracker_service = TrackerService()

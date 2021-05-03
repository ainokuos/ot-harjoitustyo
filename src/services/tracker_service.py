from entities.user import User
from entities.note import Note
from repositories.user_repository import user_repository
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

    def create_note(self, name, cr, grade):
        """ Luo uuden suorituksen.

        Args:
            name: Merkkijono, joka kuvaa suorituksen nimeä
            cr: Numeroarvo, joka kuvaa suorituksen opintopisteitä
            grade: Numeroarvo, jok kuvaa suorituksen arvosanaa
        """
        note = Note(name, cr, grade, self.user.username)
        note_repository.create(note)

    def get_notes(self):
        """ Hakee kaikki suoritukset.

            Returns:
                Lista kirjautuneen käyttäjän suorituksista
        """
        notes = note_repository.find_all()
        return [note for note in notes if note.username == self.user.username]

    def get_sum(self):
        """ Laskee opintopisteiden summan.

            Returns:
                Opintopisteiden summan
        """
        notes = self.get_notes()
        points = 0
        for note in notes:
            if note.username == self.user.username:
                points += int(note.cr)
        return points

    def get_average(self):
        """ Laskee arvosanojen keskiarvon.

            Returns:
                Arvosanojen keskiarvon pyöristettynä
                0 , jos suorituksia ei ole
        """
        notes = self.get_notes()
        grades = 0
        total = 0
        for note in notes:
            if note.username == self.user.username:
                grades += int(note.grade)
                total +=1
        if total > 0:
            return f"{(grades/total):.2F}"
        return 0

    def delete_note(self, note):
        """ Poistaa yksittäisen suorituksen.

            Args:
                note: Poistettava suoritus Note-oliona
        """
        note_repository.delete_one(note)

    def delete_notes(self):
        """ Poistaa kaikki suoritukset. """
        note_repository.delete_all()

tracker_service = TrackerService()

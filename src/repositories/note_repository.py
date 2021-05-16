from entities.note import Note
from config import NOTES_FILE_PATH
from repositories.csv_repository import CsvRepository

class NoteRepository:
    """ Luokka, joka vastaa muistiinapnojen tallennuksesta

        Attributes:
            file_path: osoite luokan käyttämään tiedostoon
    """

    def __init__(self, file_path):
        """ Luokan konstruktori, joka aloittaa tiedon tallennuksen.

            Args:
                file_path: Merkkijono, joka kuvaa tiedoston osoitetta
        """
        self._file_path = file_path
        self.csv_repository = CsvRepository(self._file_path)

    def _read(self):
        """ Lukee tiedostoa.

            Returns:
                tiedostossa olevat muistiinpanot listana
        """
        notes_list = self.csv_repository.read()
        notes = []
        for note in notes_list:
            parts = note.split(";")
            header = parts[0]
            message = parts[1]
            username = parts[2]
            notes.append(Note(header, message, username))
        return notes

    def _write(self, notes):
        """ Kirjoittaa tiedostoon

            Args:
                notes: lista tallennettavista muistiinpanoista
        """
        self.csv_repository.ensure_file_exists()
        with open(self._file_path, "w") as file:
            for note in notes:
                row = f"{note.header};{note.message};{note.username}"
                file.write(row + "\n")

    def create(self, note):
        """ Luo uuden muistiinpanon.

            Args:
                note: Note-olio muistiinpanosta
        """
        notes = self.find_all()
        notes.append(note)
        self._write(notes)

    def find_all(self):
        """ Hakee kaikki muistiinpanot. """
        return self._read()
    
    def delete_one(self, note):
        """ Poistaa yksittäisen muistiinpanon.

            Args:
                note: Note-olio poistettavasta muistiinpanosta
        """
        notes = self.find_all()
        for i in notes:
            if note.message == i.message and note.username == i.username:
                notes.remove(i)
                self._write(notes)
                break

    def delete_all(self):
        """ Poistaa kaikki muistiinpanot. """
        self.csv_repository.delete_all()

note_repository = NoteRepository(NOTES_FILE_PATH)
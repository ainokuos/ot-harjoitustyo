from entities.note import Note
from config import NOTES_FILE_PATH
from repositories.csv_repository import CsvRepository

class NoteRepository:

    def __init__(self, file_path):
        self._file_path = file_path
        self.csv_repository = CsvRepository(self._file_path)

    def _read(self):
        rows = self.csv_repository.read()
        notes = []
        for row in rows:
            parts = row.split(";")
            header = parts[0]
            message = parts[1]
            username = parts[2]
            notes.append(Note(header, message, username))
        return notes

    def _write(self, notes):
        self.csv_repository.ensure_file_exists()
        with open(self._file_path, "w") as file:
            for note in notes:
                row = f"{note.header};{note.message};{note.username}"
                file.write(row + "\n")

    def create(self, note):
        notes = self.find_all()
        notes.append(note)
        self._write(notes)
        return note

    def find_all(self):
        return self._read()
    
    def delete_one(self, note):
        notes = self.find_all()
        for i in notes:
            if note.message == i.message and note.username == i.username:
                notes.remove(i)
                self._write(notes)
                break

    def delete_all(self):
        self.csv_repository.delete_all()

note_repository = NoteRepository(NOTES_FILE_PATH)
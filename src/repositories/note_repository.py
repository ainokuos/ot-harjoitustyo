from pathlib import Path
from entities.note import Note
from config import NOTES_FILE_PATH

class NoteRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        notes = []
        self._ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                name = parts[0]
                cr = parts[1]
                grade = parts[2]
                username = parts[3]
                notes.append(Note(name,cr,grade, username))
            return notes

    def _write(self, notes):
        self._ensure_file_exists()
        with open(self._file_path, "w") as file:
            for note in notes:
                row = f"{note.name};{note.cr};{note.grade};{note.username}"
                file.write(row+"\n")

    def create(self, note):
        notes = self.find_all()
        notes.append(note)
        self._write(notes)
        return note 

    def find_all(self):
        return self._read()

    def delete_all(self):
        self._ensure_file_exists()
        with open(self._file_path, "w") as file:
            file.write("")

    def delete_one(self, note):
        notes = self.find_all()
        for i in notes:
            if note.name == i.name and note.username == i.username:
                notes.remove(i)
                self._write(notes)
                break
note_repository = NoteRepository(NOTES_FILE_PATH)
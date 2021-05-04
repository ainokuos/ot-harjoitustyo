from pathlib import Path

class CsvRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def ensure_file_exists(self):
        Path(self._file_path).touch()

    def delete_all(self):
        self.ensure_file_exists()
        with open(self._file_path, "w") as file:
            file.write("")

    def read(self):
        rows = []
        self.ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                rows.append(row)

        return rows



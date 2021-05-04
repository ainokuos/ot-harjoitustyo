from pathlib import Path

class CsvRepository:
    """ Luokka, joka vastaa csv-tallennuksesta.

        Attributes:
            file_path: tallennettavan tiedoston osoite
    """
    def __init__(self, file_path):
        """ Luokan konstruktori, joka aloittaa uuden tallennuksen tietokantaan.

            Args:
                file_path: osoite käytössä olevaan tiedostoon
        """
        self._file_path = file_path

    def ensure_file_exists(self):
        """ Tarkistaa onko tiedosto olemassa ja luo uuden tarvittaessa. """
        Path(self._file_path).touch()

    def delete_all(self):
        """ Tyhjentää tiedoston. """
        self.ensure_file_exists()
        with open(self._file_path, "w") as file:
            file.write("")

    def read(self):
        """ Lukee tiedoston sisällön.

            Returns:
                rows: lista tiedoston riveistä
        """
        rows = []
        self.ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                rows.append(row)

        return rows



from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    """Palauttaa käyttäjän.

        Args:
            row: halutun käyttäjän sisältävä rivi tietokannasta
        Returns:
            User: User-oliona etsitty käyttäjä
            None: jos käyttäjää ei ole
    """
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    """ Luokka, joka vastaa käyttäjien tallennuksesta tietokantaan.

        Attributes:
            connection: yhteys tietokantaan
    """
    def __init__(self, connection):
        """ Luokan konstruktori, joka aloittaa uuden tallennuksen tietokantaan.

            Args:
                connection: Yhteys SQLite-tietokantaan
        """
        self._connection = connection

    def create(self, user):
        """ Luo uuden käyttäjän.

            Args:
                user: User-olio luodusta käyttäjästä
            Returns:
                user: User-olio luodusta käyttäjästä
        """
        cursor = self._connection.cursor()

        cursor.execute("insert into users(username,password)values(?,?)",(user.username,user.password))

        self._connection.commit()

        return user

    def find_by_username(self, username):
        """ Hakee käyttäjää tunnuksen perusteella.

            Args:
                username: Merkkijono haettavan käyttäjän tunnuksesta
            Returns:
                get_user_by_row(): kutsuu funktiota, joka palauttaa käyttäjän User-oliona
        """
        cursor = self._connection.cursor()

        cursor.execute(" select * from users where username = ?", (username, ))

        row = cursor.fetchone()

        return get_user_by_row(row)

    def find_all(self):
        """ Hakee kaikki käyttäjät.

            Returns:
                list(get_user_by_row()): lista käyttäjistä User-olioina
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))
    
    def delete_all(self):
        """ Poistaa kaikki käyttäjät. """
        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()

user_repository = UserRepository(get_database_connection())

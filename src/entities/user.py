class User:
    """ Luokka, joka kuvaa yksittäistä käyttäjää

    Attributes:
        username: Käyttäjän tunnus
        password: Käyttäjän salasana
    """

    def __init__(self, username, password):
        """ Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän tunnusta
            password: Merkkijono, joka kuvaa käyttäjän salasanaa
        """

        self.username = username
        self.password = password

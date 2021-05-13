class Note:
    """ Luokka, joka kuvaa yksittäistä muistiinpanoa

        Attributes:
            header: Kuvaa muistiinpanon aihetta
            message: Kuvaa muistiinpanon sisältöä
            username: Kuvaa muistiinpanon lisännyttä käyttäjää
        """
    def __init__(self, header, message, username):
        """ Luokan konstruktori, joka lisää uuden muistiinpanon:

            Args:
                header: Merkkijono, joka kuva muistiinpanon otsikkoa
                message: Merkkijono, joka kuvaa muistiinpanon sisältöä
                username: User-olio, joka kuvaa muistiinpanon lisännyttä käyttäjää
        """
        self.header = header
        self.message = message
        self.username = username
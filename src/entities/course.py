class Course:
    """ Luokka, joka kuvaa yksittäistä opintosuoritusta

    Attributes:
        name: Suoritukset/kurssin nimi
        cr: Suorituksen opintopisteet
        grade: Suorituksen arvosana
        username: Suorituksen lisänneen käyttäjän tunnus
    """

    def __init__(self, name, cr, grade, username):
        """ Luokan konstuktori, joka luo uuden suorituksen

        Args:
            name: Merkkijono, joka kuvaa suorituksen nimeä
            cr: Numeroarvo, joka kuvaa suorituksen opintopisteitä
            grade: Numeroarvo, joka kuvaa suorituksen arvosanaa
            username: User-olio, joka kuvaa suorituksen lisännyttä käyttäjää
        """
        
        self.name = name
        self.cr = cr
        self.grade = grade
        self.username = username


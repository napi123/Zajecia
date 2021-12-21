from dane.dieta import Dieta


class Pacjent:

    def __init__(self, imie: str, nazwisko: str, mail: str, dieta: Dieta):
        self._imie = imie
        self._nazwisko = nazwisko
        self._mail = mail
        self._dieta = dieta

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def mail(self):
        return self._mail

    @property
    def dieta(self):
        return self._dieta

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

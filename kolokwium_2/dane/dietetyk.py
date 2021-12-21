
class Dietetyk:

    def __init__(self, imie: str, nazwisko: str, nr_telefonu: int, mail: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_telefonu = nr_telefonu
        self._mail = mail

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def nr_telefonu(self):
        return self._nr_telefonu

    @property
    def mail(self):
        return self._mail

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

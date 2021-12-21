
class Dieta:

    def __init__(self, rodzaj_diety: str, cena: float, kalorie: int,
                 okres_diety: str):
        self._rodzaj_diety = rodzaj_diety
        self._cena = cena
        self._kalorie = kalorie
        self._okres_diety = okres_diety

    @property
    def rodzaj_diety(self):
        return self._rodzaj_diety

    @property
    def cena(self):
        return self._rodzaj_diety

    @property
    def kalorie(self):
        return self._kalorie

    @property
    def okres_diety(self):
        return self._okres_diety

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

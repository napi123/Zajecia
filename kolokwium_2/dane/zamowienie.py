from datetime import datetime
from dane.dieta import Dieta
from dane.dietetyk import Dietetyk
from dane.pacjent import Pacjent


class Zamowienie:

    _nr_zamowienia: int
    _data_zamowienia: datetime
    _pacjent: Pacjent
    _dietetyk: Dietetyk
    _dieta = list[Dieta]

    def __init__(self) -> None:
        pass

    @property
    def nr_zamowienia(self):
        return self._nr_zamowienia

    @nr_zamowienia.setter
    def nr_zamowienia(self, nr_zamowienia: int):
        self._nr_zamowienia = nr_zamowienia

    @property
    def data_zamowienia(self):
        return self._data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, data_zamowienia: datetime):
        self._data_zamowienia = data_zamowienia

    @property
    def pacjent(self):
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self._pacjent = pacjent

    @property
    def dietetyk(self):
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk: Dietetyk):
        self._dietetyk = dietetyk

    @property
    def dieta(self):
        return self._dieta

    @dieta.setter
    def dieta(self, dieta: list[Dieta]):
        self._dieta = dieta

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def wartosc_diet(self):
        show_wartosc: float = 0
        for x in self._dieta:
            show_wartosc += x.cena
        return round(show_wartosc, 2)

    def liczba_kal(self):
        kalorie: int = 0
        for x in self.dieta:
            kalorie += x.kalorie
        return kalorie

class Hurtownia:
    def __init__(self, marka, ilosc:int, jakosc, cena):
        self.marka=marka
        self.ilosc=ilosc
        self.jakosc=jakosc
        self.cena=cena
    def __str__(self):
        return f'Marka: {self.marka}, Ilosc: {self.ilosc}, Jakośc: {self.jakosc}, Cena: {self.cena}'

class Produkt(Hurtownia):
    def __init__(self, marka, ilosc:int, jakosc, cena, typ):
        self.marka = marka
        self.ilosc = ilosc
        self.jakosc = jakosc
        self.cena = cena
        self.typ = typ
    def __str__(self):
        return super().__str__() + ', Typ:' + str(self.typ)

class Magazyn(Hurtownia):
    def __init__(self, marka, ilosc:int, jakosc, cena, lokalizacja):
        self.marka = marka
        self.ilosc = ilosc
        self.jakosc = jakosc
        self.cena = cena
        self.lokalizacja = lokalizacja
    def __str__(self):
        return super().__str__() + ', Lokalizacja magazynu:' + str(self.adres)

class KlientDetaliczny(Hurtownia):
    def __init__(self,marka, ilosc:int, jakosc, cena, odbiorca):
        self.marka = marka
        self.ilosc = ilosc
        self.jakosc = jakosc
        self.cena = cena
        self.odbiorca = odbiorca
    def __str__(self):
        return super().__str__() + ', Odbiorca:' + str(self.odbiorca)

class Zamowienia(Hurtownia):
    def __init__(self, marka, ilosc:int, jakosc, cena, adres, do_wyslania):
        self.marka = marka
        self.ilosc = ilosc
        self.jakosc = jakosc
        self.cena = cena
        self.adres = adres
        self.do_wyslania= do_wyslania
    def __str__(self):
        return super().__str__() + ', Adres:' + str(self.adres)

    def wartosc(self):
        for x in self.cena:
            return sum(self.cena)
            print(round(self.cena, 2))

    def adres_klienta(self):
        return self.adres if self.do_wyslania is True else False

class KlientBiznasowy(Hurtownia):
    def __init__(self, marka, ilosc:int, jakosc, cena, imie_klienta):
        self.marka = marka
        self.ilosc = ilosc
        self.jakosc = jakosc
        self.cena = cena
        self.imie_klienta=imie_klienta
    def __str__(self):
        return super().__str__() + ', Imie klienta:' + str(self.imie_klienta)

zamowienie = Zamowienia('Sony',5,'fabrycznie nowy','1000 zł','Pola 15',True)
print(zamowienie)
print(zamowienie.adres_klienta())
print(zamowienie.wartosc())
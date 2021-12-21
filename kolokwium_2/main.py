from dane.dieta import Dieta
from dane.dietetyk import Dietetyk
from dane.pacjent import Pacjent
from dane.zamowienie import Zamowienie
from datetime import datetime


dieta1 = Dieta('wysokobiałkowa', 300, 3000, '3 miesiące')
pacjent1 = Pacjent('Adam', 'Małysz', 'malysz@wp.pl', dieta1)
dietetyk1 = Dietetyk('Jan', 'Kowalski', 568096543, 'jan@o2.pl')

z1 = Zamowienie()
z1.nr_zamowienia = 1
z1.data_zamowienia = datetime(2021, 12, 10)
z1.pacjent = pacjent1
z1.dietetyk = dietetyk1

print(z1)

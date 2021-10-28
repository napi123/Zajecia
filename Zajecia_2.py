# Zadanie 2a
def zadanie2a(lista):
    for x in lista:
        print(x)
list1 = ["Tom","Eva","Anna","Adam","Ola"]
zadanie2a(list1)


# Zadanie 2b pentla for
def zadanie2b1(lista):
    for x in lista:
        print(x*2)
l2=[3,2,3,5,1]
zadanie2b1(l2)

# Zadanie 2b lista
def zadanie2b2(lista):
    listab = [2*x for x in lista]
    print(listab)
zadanie2b2(l2)


# Zadanie 2c
def zadanie2c():
    for x in range(10):
        if x%2==0:
            print(x)
zadanie2c()


# Zadanie 2d
def zadanie2d():
    for x in range(0,10,2):
        print(x)
zadanie2d()
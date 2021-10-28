#zad1
def zad1(name:str, surname:str):
    return "Cześć "+ name + " " + surname + "!"
msg = zad1("Adrian","Naplocha")
print(msg)

#Zad2
def zad2(a:int, b:int):
    return a*b
print(zad2(3,7))

#Zad3
def zad3(a:int):
    return True if a%2==0 else False
check:bool = zad3(5)
if check==True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

#Zad4
def zad4(a:int, b:int, c:int):
    return True if a+b>=c else False
print(zad4(3,6,5))

#Zad5
def zad5(l1:list,x:int):
    return True if x in l1 else False
print(zad5([1,2,3,4,5],7))

#Zad6
def zad6(l1:list, l2:list):
    for a in l2:
        if a not in l1:
            l1.append(a)
    for x in range(len(l1)):
        l1[x]=l1[x]**2
    return l1
print(zad6([1,2,3,4,5],[2,3,4,6,7]))
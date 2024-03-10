# l1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2=[]
# for i in l1:
#     l2.append(i**2)
# print(l2)
# l2=[i**2 for i in l1]
# print(l2)
# l3=[3**y for y in range(1,6)]
# print(l3)
# l4=[x for x in l1 if x%2==1]
# print(l4)
# l5=[(x,y) for x in l2 for y in l3]
# print(l5)
#
# l6=[]
# for i in l2:
#     for j in l3:
#         l6.append((i,j))
# print(l6)

# s1= {1: 2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9}
# s2={}
# for key, value in s1.items():
#     s2[value] = key
# print(s2)
# s3={v:k for k, v in s1.items()}
# print(s3)
from math import *
# albo import math

# def rownanie_kwadratowe(a, b, c):
#     delta = b**2-4*a*c
#     if delta<0:
#         print("Brak pierwiastkow")
#         return 0
#     elif delta ==0:
#         print("Jeden pierwiastek")
#         x=(-b)/(2*a)
#         return x
#     elif delta>0:
#         print("Dwa pierwiastki")
#         x1=(-b + math.sqrt(delta))/(2*a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
# print(rownanie_kwadratowe(6, 3, 1))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(2, 6, 1))

# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return sqrt((x1-x2)**2 + (y1-y2)**2)
#
# print (dlugosc_odcinka())
# print (dlugosc_odcinka(3, 5, 1, 6))
# print (dlugosc_odcinka(y1=5, x1=3, y2=6, x2=8))
# print (dlugosc_odcinka(1, 5, y2=8, y1=3))

# plik = open('tekst.txt', 'r', encoding='utf-8')
# plik.read(10)
# linia= plik.readline()
# linie = plik.readlines()
# plik.close()
# print(znak)
# print(linia)
# print(linie)


# plik= open('tekst.txt', 'a+')
# plik.write('git')
# znaki= plik.read(10)
# plik.seek(105)
# plik.close
# print(znaki)

# with open ('tekst.txt', 'r') as plik:
#     znaki=plik.read(10)
# print (znaki)

#ZADANIA~-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

a = [1-x for x in range(1, 10)]
b = [4**i for i in range(8)]
c = [x for x in b if x % 2 == 0]

print(a)
print(b)
print(c)

import random
lista1 = [random.randint(1, 100) for _ in range(10)]
print(lista1)
lista2 = [i for i in lista1 if i % 2 == 0]
print(lista2)

produkty = {"piwo":"ml", "wodka":"ml", "papierosy":"szt", "mleko":"ml", "mieso":"kg", "lizaki":"szt", "batony":"szt" }
print(produkty)
produkty_na_sztuki = [produkt for produkt, jednostka in produkty.items() if jednostka == 'szt']
print(produkty_na_sztuki)

def prostokatny(a, b, c):
    if(a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2):
        return("Trojkat jest prostokatny")
    else:
        return("Trojkat nie jest prostokatny")

a = float(input("Podaj wartosc a: "))
b = float(input("Podaj wartosc b: "))
c = float(input("Podaj wartosc c: "))

print(prostokatny(a,b,c))

#Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.

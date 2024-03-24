# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = 'Wizualizacja danych'
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))
#
# a = 6
# b = 3
#
# c = a + b
# print(c)
# d = a - b
# print(d)
# e = 4
# f = b//a
# print(f)
# f = a//b
# print(f)
# g = a ** 2
# print(g)
# h = pow(a, 2)
# print(h)
#
# i = 6 ** (1/2)
# j = pow(6, 1/2)
# print(i)
# print(j)
#
# k = 'Wizualizacja danych'
# l = ' grupa 1'
# m = 1
# print(k+l)
# print('liczba a jest rowna {:.3f}, liczba b jest rowna {}'
#       .format(a, b))
#
# a=input('Wprowadz liczbe: ')
# print (a)
# print(type(a))
# print(a*5)
# print(type(a))
#
# import sys
#
# sys.stdout.write('Wprowadz liczbe: ')
# b = sys.stdin.readline()
# print(b)
# print(type(b))

#lista = [5, 6.6, 34, 'a', 'b', [2, 3,4], 'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2, 'c')
# print(lista)
# lista.extend([20, 21, 22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2,3,4])
# print(lista)
# del lista[1]
# print(lista)
# lista.reverse()
# print(lista)
# lista.sort()  #tylko liczby nie mozna sortowac stringow z intami
# print(lista)

# slownik = {'klucz': 'wartosc', 1: 2, 'a':5, 4: 'b'}
# print(slownik)
# print(slownik[4])
# slownik[6]=45
# print(slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]
# print(slownik)


# a = 8
# b = 8
#
# if a>b:
#       print("a is greater than b")
# elif a<b:
#       print("a is less than b")
# else:
#       print("a is equal to b")


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if(a>b) & (b>d):
#       print(a, c)
# else:
#       print(b,d)

# for i in range(8):
#       print(i)
# else:
#       print('koniec petli')

# for i in lista:
#       print(i)

# for i in range(0,5):
#       for j in range(0,5):
#             result = i+j
#             print(result)
#       print(' ')

# licznik = 0
# while licznik < len(lista):
#       print(lista[licznik])
#       licznik +=1
# else:
#       print('koniec petli')

# licznik = 0
# while licznik != 10:
#       if licznik == 7:
#             print(licznik)
#             break
#       else:
#             licznik += 1
# else:
#       print(licznik)

# lista = [3,5,6,12]
# import sys
#
# sys.stdout.write('Wprowadz liczbe: ')
# a = sys.stdin.readline()
# a = int(a)
# i=0
# while i<len(lista):
#       if a-lista[i]==0:
#             print(i, lista[i])
#             break
#       else:
#             i+=1
# else:
#       print('Nie ma takiej liczby')

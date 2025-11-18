#Jak nie programować wielokrotnie powtarzalnych czynności


"""a= int(input('Podaj pierwszą liczbę:'))
b = int(input('Podaj drugą liczbę:'))
c = int(input('Podaj trzecią liczbę:'))
d = int(input('Podaj czwartą liczbę:'))
e = int(input('Podaj piątą liczbę:'))

suma = (a + b + c + d + e)

print(suma)"""


"""liczba = 0
suma = 0

for i in range(5):
    liczba = float(input('Podaj liczbę'))
    suma = suma + liczba
    
print(suma)"""

#Listy
'''lista = ['qwerty', 56, [6, 7], 4.56, [[5,8], 1]]
print(lista[2][1])
print(lista[4][0][1])'''

# Listy i pętle
'''lista2 = ['kot', 'pies', 'owca', 'lama']

# Pętla for wyciąga dame z listy (jedna po drugiej)
#Pętla wykonuje się tyle razy ile elementów ma lista

for z in lista2:
    print(z)

#Pętla która wykona sie trzy razy
lista3 = [1410, 15, 7]

for i in lista3:
    print('OK')


#Pętla, która wykonuje się 10 razy'''
'''lista4 = [0] * 10
print(lista4)

for i in lista4:
    print('CZEŚĆ')

#3 Generatory i pętle
przedzial = range(1, 10)

for i in przedzial:
    print(i)

#Pętla która wykona się 10 razy
for i in range(10): #range(0, 10), 10 - liczba powtórzeń
    print(i)'''


'''lista5 = [0]
lista5.append(0)
print(lista5)'''

#infinity
'''lista = [0]

for i in lista:
    print('Cześć')
    lista.append(5)

#Pętla while'''

liczba = 5

while liczba > 0:
    print(liczba)
    liczba = liczba - 1




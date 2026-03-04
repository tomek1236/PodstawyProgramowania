#Zadanie 1
'''slowo = 'npsiotvobumnigaasdfgrbnymukuloooojhtgdv'
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
slowo2 = ''.join([x for x in list(slowo) if x not in samogloski])
print(slowo2)'''

#Zadanie 2
'''zagniezdzona = lista2[5][1:4]
print(zagniezdzona)
#Zadanie 3
suma = 0
lista_liczb = list(map(int, liczby))
print(sum(lista_liczb))
#Zadanie 4
for i in range(len(lista2d)):
    element = lista2d[i][i]
    suma += element
print(suma)'''

#Zadanie 5
'''for o in oceny:
    print(o, len(oceny[o]))

    for uczen in oceny[1]
        oceny[2].append(uczen)
    del oceny[1]
    for uczen1 in oceny[6]
        oceny[5].append(uczen1)
    del oceny[6]
print(oceny)'''

#Zadanie 6
from collections import Counter
liczba = input('Podaj l.c.d')
cyfry = list(liczba)
#a)
print(len(cyfry))

#b)
zbior = set(cyfry)
print(len(zbior))

#c)
a = Counter(cyfry)

for e in zbior:
    print(f'{e}: {cyfry.count(e)}')
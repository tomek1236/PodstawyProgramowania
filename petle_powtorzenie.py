lista = [10, 56, 89, 59]

#1. Chodzenie bezpośrednio po elementach listy
# Do zmiennej b trafiają bezposrednio elementy listy, tzn. 10, 56, 89, 59
for b in lista:
    print(b)

#2. Chodzenie po liscie z użyciem inekdsów
#2.1 co to jest indeks?
# lista[2]
# 2 - indeks
# lista[2] - element znajdujący pod indeksem 2 = 89

#2.2
for k in range(4):
    print(lista[k])
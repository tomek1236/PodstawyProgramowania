#Pętla while - przykłady
from time import sleep

liczba = 120
licznik = 0
# pętl while podajemy warunek TRWANIA pętli
while liczba > 0: #tak długo jak liczba jest dodatnia, pętla sięwykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)


#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć')
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakonczyć')
print(licznik)'''


#Zadanie 2
'''popr_haslo = 'informatyka'

haslo = input('Podaj hasło: ')
proba = 1
while haslo != popr_haslo and proba <= 5:
    print('Hasło błedne, podaj raz jeszcze')
    haslo = input('Podaj hasło')
    proba = proba + 1
if haslo == popr_haslo:
   print('Witaj w systemie')
else:
    print('Nie ma hasła nie ma systemu ')'''


#zadanie 3
#w trakcie gdy n jest wieksze lub rowne od 0 to odejmujemy 1, gdy liczba jest nieparzysta to dalej odejmujemy
# wszystko sie sumuje w jeden wynik czyli 20 + 18 + 16 + 14 + 12 + 10 + 8 + 6 + 4 + 2 + 0 - 2 = 108

#zad 4
#for i in range(10, 0, -1):
   #print(i)

   #wwwwwwwww
'''wynik1 = 0
wynik2 = 0
akcja = 0
from random import randint
while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2):
    akcja += 1
    print(f'Akcja {akcja}')
    #druzyna = int(input('Podaj nr drużyny, która wygrała akcję'))
    druzyna = randint(1, 2)
    if druzyna == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(111)
if wynik1 > wynik2:
    print('Wygrała druzyna 1')
else:
    print('Wygrala druzyna 2')'''


#Zadanie 7
'''liczba = int(input('Podaj liczbe'))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

# Zadanie 8
liczba = int(input('Podaj liczbe'))
d = 2
ile_r_czyn = 0
ile_czyn = 0

while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba = liczba // d
    ile_czyn += 1
    d += 1
print(ile_czyn)

x = 0
y = 0
koniec = False

while not koniec:
    print("Wykonaj ruch")
    ruch = input().lower()

    if ruch == 'q':
        print("Koniec")
        koniec = True
    else:
        nx, ny = x, y

        if ruch == 'g':      # góra
            ny += 1
        elif ruch == 'd':    # dół
            ny -= 1
        elif ruch == 'p':    # prawo
            nx += 1
        elif ruch == 'l':    # lewo
            nx -= 1
        else:
            print("Nieznany ruch")
            continue

        if 0 <= nx <= 9 and 0 <= ny <= 9:
            x, y = nx, ny
            print(f"({x}, {y})")
        else:
            print("Niemozliwe")

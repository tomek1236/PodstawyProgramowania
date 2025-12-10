#Pętla while - przykłady

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
popr_haslo = 'informatyka'

haslo = input('Podaj hasło: ')
proba = 1
while haslo != popr_haslo and proba <= 5:
    print('Hasło błedne, podaj raz jeszcze')
    haslo = input('Podaj hasło')
    proba = proba + 1
if haslo == popr_haslo:
   print('Witaj w systemie')
else:
    print('Nie ma hasła nie ma systemu ')


#zadanie 3
#w trakcie gdy n jest wieksze lub rowne od 0 to odejmujemy 1, gdy liczba jest nieparzysta to dalej odejmujemy
# wszystko sie sumuje w jeden wynik czyli 20 + 18 + 16 + 14 + 12 + 10 + 8 + 6 + 4 + 2 + 0 - 2 = 108

#zad 4
#for i in range(10, 0, -1):
   #print(i)

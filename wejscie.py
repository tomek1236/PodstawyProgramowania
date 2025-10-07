#1. Wprowadzanie danych przez użytkownika do programu

#1) utworzenie zmiennej
#2) na ekranie pojawia się komunikat z inputa
#3) program się zatrzymuje i czeka na podanie danych i zatwierdzenie tego ENTEREM
#4) po wpisaniu i zatwierdzeniu ENTEREM to co wpiszemy trafia jako string do zmiennej
imie = input('Podaj swoje imie')

liczba = int(input('podaj liczbe'))
print(type(liczba))

liczba_z_przecinkiem = float(input('Podaj liczbe z przecinkiem'))
print(type(liczba_z_przecinkiem))

cos = list(input('podaj coś'))
print(cos)
print(type(cos))
plik = open('liczby.txt')
dane = plik.readlines()

for x in range(len(dane)):
    dane[x] = dane[x].strip()

for x in dane:
    if int(x[::-1]) % 17 == 0:
        print(x[::-1])


print(len(set(dane)))

licznik = 0
for i in set(dane):
    if dane.count(i) == 2:
        licznik += 1
print(licznik)

licznik1 = 0
for i in set(dane):
    if dane.count(i) == 3:
        licznik1 += 1
print(licznik1)




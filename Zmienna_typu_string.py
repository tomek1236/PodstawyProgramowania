napis = 'informatyka'

#I. Fragment tekstu:
#1) wycinanie od .... do
print(napis[2:5]) #czyli tak naprawde od 2 do 4

#2) wycinanie od .... do co ileś
print(napis[2:10:2])

#3) wycinanie od początku
print(napis[:3])

#4) wycinanie od kónca
print(napis[7:])

#5) czytanie od końca
print(napis[::-1])

#II. Zawieranie się znaku w słowie
if 'a' in napis:
    print('należy')
else:
    print('nie należy')
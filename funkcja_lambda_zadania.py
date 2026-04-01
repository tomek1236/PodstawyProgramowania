#Zadanie 1.1
lista = [4, 10, 12, 9, 5]
potegi = [(x, x ** 2, x ** 3, x ** 4)for x in lista]
print(potegi)

#Zadanie 1.2
potegi2 = list(map(lambda x: (x, x ** 2, x ** 3, x ** 4 ), lista))
print(potegi2)

#Zadanie 1.3

lista_dat = ['20241101', '20231223', '20220711', '20230503']
lista_dat_slowniki = list(map(lambda x: {'rok': int(x[0:4]), 'miesiac':int(x[4:6]) , 'dzien':int(x[6:])}, lista_dat))
print(lista_dat_slowniki)

#Zadanie 2.1
class Galeria:
    def __init__(self, kraj, miasto, lokale_handlowe):
        self.kraj = kraj
        self.miasto = miasto
        self.lokale_handlowe = lokale_handlowe


g1 = Galeria('PL', 'Gdańsk', [(4, 6), (6, 10), (11, 9)])

print(g1.kraj, g1.miasto, g1.lokale_handlowe[1][1])

#Zadanie 2.2
plik = open('galerie.txt')
dane = plik.readlines()
Galerie = []
for x in dane:
    x = x.split()
    kraj = x[0]
    miasto = x[1]
    lokale_handlowe = [(int(d), int(s)) for d, s in zip(x[2::2], x[3::2])]
    Galerie.append(Galeria(kraj, miasto, lokale_handlowe))

for g in Galerie:
    print(g.kraj, g.miasto, g.lokale_handlowe)


galerie_sort = list(sorted(Galerie, key = lambda x: x.miasto))

for g in galerie_sort:
    print(g.kraj, g.miasto, g.lokale_handlowe)

#Zadanie X
#Sortowanie listy galerii według pola powierzchni pierwszego lokalu
galerie_sort2 = list(sorted(Galerie, key = lambda x: x.lokale_handlowe[0][0] * x.lokale_handlowe[0][1]))



#Zadanie 2.4
def powierzchnia_galerii(galeria):
    lista_lokali = galeria.lokale_handlowe
    suma = 0
    for p in lista_lokali:
        pole = p[0] * p[1]
        suma += pole
    return suma



galerie_sort_powierchnie = list(sorted(Galerie, key = lambda x: powierzchnia_galerii(x)))

for g in galerie_sort_powierchnie:
    print(g.kraj, g.miasto, g.lokale_handlowe)


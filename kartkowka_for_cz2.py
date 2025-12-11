'''n = int(input('Podaj liczbe'))

iloczyn = 1
for x in range(n):
    iloczyn = iloczyn * (x + 1)

print(iloczyn)'''



lista = [4, 12, 8, 1, 5, 6, 3]
licznik = 0
for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x] != lista[y] and (lista[x] + lista[y]) % 3 == 0:
         #print(f'({lista[x]},{lista[y]})')
         licznik = licznik + 1
print(licznik)



n = int(input('podaj ile będzie napisów'))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
    print(max_napis)



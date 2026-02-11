zbior = {5, 6, 6, 1, 1, 5, 9}
print(zbior)

zbior2 = {'kot', "pies", 'gołąb', 'kot', 'pies'}
print(len(zbior2))

a = set(range(0, 20, 2))
print(a)
b = {1, 2, 3, 4, 6, 12}

#suma zbiorow
suma_A_B = a.union(b)
print(suma_A_B)

suma_A_B2 = set(list(a) + list(b))
print(suma_A_B2)

#część wspolna zbiorów
iloczyn_a_b = a.intersection(b)
print(iloczyn_a_b)

#róznica
roznica_a_b = a.difference(b)
print(roznica_a_b)

#Dodawanie elementu do zbioru
C = {1, 7, 4, 5}
C.add(2)
print(C)



lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]

# a)
print(lista2[1][2])

# b)
mrowka = list(lista2[3])
print(mrowka[2])


#odwrotnie
slowo = ''.join(mrowka)
print(slowo)

# c)
lista3 = lista1[2::2]
print(lista3)

# d)
lista2.append(lista2[1] * 3)
print(lista2)

# e)
lista1 = lista1 + [9, 6, 16, -8, 7]
print(lista1)

# f)

#lista1.sort()
lista1_posortowana = sorted(lista1)
print(lista1_posortowana)

print(lista1_posortowana[0], lista1_posortowana[-1])

#min i max
print(min(lista1), max(lista1))

# g)
'''del lista1[4]
print(lista1)'''

# h)
del lista1[4:9]
print(lista1)

# i)
while 2 in lista1:
    lista1.remove(2)

print(lista1)

#j)
'''lista3 = [x ** 2 for x in lista1]

print(lista3)'''
lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)

#Zadanie 2
'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

x_max = max(lista)
x_min = min(lista)

lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)'''

#Zadanie 3
lista = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
'''lista = [x for x in lista if x > 1000 or x < 9999]'''
print(lista)
lista = [x for x in lista not (x >= 1000 and x <= 9999)]

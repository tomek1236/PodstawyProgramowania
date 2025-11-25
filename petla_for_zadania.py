#Zadanie 15
'''X = list(range(0, 103, 3))
print(X)

print(f'x\ty')
for x in X:
    y = 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')'''

#b)
"""print(f'x\t\ty')
for x in range(-30, 61):
    x = x / 10
    y = 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')"""

#Zadanie 16
lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))

#Sposób 1
'''for x, y, z in zip(lista1, lista2, lista3):
    print(f'{x}\t{y}\t{z}')'''

#Sposób 2
for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')
suma = 0
# Zadanie 17
n = int(input('Podaj ile bedzie liczb'))
for i in range(n):
    liczba = int(input('Podaj liczbe'))
    suma = suma + liczba
    print(suma)
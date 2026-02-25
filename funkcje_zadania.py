def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w


u = [2, 7, 3]
v = [-1, 0, 4]

wynik = suma_v(u, v)
print(wynik)

def iloczyn_sk(u, v):
    a = []
    for y in range(len(u)):
        iloczyn = u[y] * v[y]
        a.append(iloczyn)
    return sum(a)

u = [2, 7, 3]
v = [-1, 0, 4]

wynik1 = iloczyn_sk(u, v)
print(wynik1)



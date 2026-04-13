'''t = 0
chwila = 1
while t <= 10:
    x = 2 * t - 6
    y = 4 * t - 5 * t ** 2
    if (chwila - 1) % 200 == 0:
        print(x, y)
    t += 0.01
    chwila += 1'''''



#Zadanie 4
plik = open('sily.txt')
dane = plik.readlines()

max_F = []
najwieksza_sila = 0
for i in range(len(dane)):
    dane[i] = dane[i].split()
    dane[i][0] = float(dane[i][0])
    dane[i][1] = float(dane[i][1])
    '''sila = 0.5 ** (dane[i][0] ** 2 + dane[i][1] ** 2)
    if sila > najwieksza_sila:
        najwieksza_sila = sila'''

for F in dane:
    sila = (F[0] ** 2 + F[1] ** 2) ** 0.5
    if sila > najwieksza_sila:
        najwieksza_sila = sila
        max_F = F
print(dane)
print(najwieksza_sila)
print(max_F)

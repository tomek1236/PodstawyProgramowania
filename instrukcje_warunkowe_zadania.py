#Rozwiązywanie równania kwadratowego

# a = float(input('Podaj liczbe a =/= 0'))
# b = float(input('Podaj liczbe b =/= 0'))
# c = float(input('Podaj liczbe c =/= 0'))
#
# delta = b ** 2 - 4 * a * c
# if delta > 0:
#     x1 = (-b - delta ** 0.5) / (2 * a)
#     x2 = (-b + delta ** 0.5) / (2 * a)
#     print(f'x1 == {x1} v x2 == {x2}')
# elif delta == 0:
#     x = (-b) / (2 * a)
#     print('x1 == x2 = {}'.format(x))
# else:
#     print('brak rozwiązań')

#Zadanie 12
pisemny_j_polski = int(input('Pisemny Polski'))
pisemny_j_obcy = int(input('Pisemny obcy'))
pisemny_dodatkowy = int(input('Pisemny dodatkowy'))
ustny_j_polski = int(input('ustny polski'))
ustny_j_obcy = int(input('ustny obcy'))

if pisemny_j_polski >= 30 and pisemny_j_obcy >= 30 and pisemny_dodatkowy >= 30 and ustny_j_polski >= 30 and ustny_j_obcy >= 30:
    print('zdałeś bez amnestii!')
elif (pisemny_j_polski + pisemny_j_obcy + pisemny_dodatkowy + ustny_j_obcy + ustny_j_obcy) / 5 >= 30:
    print('zdałeś z amnestią')
else:
    print('nie zdałes!')
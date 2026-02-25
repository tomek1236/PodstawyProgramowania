def hurra():
    print('hurra\n' * 50)

hurra()

#hurra2 - nazwa funkcji
#n - parametr funkcji
#6 - argument funkcji
#hurra2(6) wywołanie funkcji dla argumentu n = 6

def hurra2(n):
    print('hurra\n' * n)

hurra2(5)

def hurra3(n = 10):
    print('hurra\n' * n)

hurra3()

#Jeżeli funkcja po prostu wykonuje jakąś czynność i nie możemy wykorzystac dalej
#efektów jej pracy jest procedura

#Pole całkowite gransiatosłupa prawidłowego trójkątnego

def p_tr_rown(a):
    '''print(a ** 2 * (3 ** 0.5) / 4)

p_tr_rown(3 ** 0.25)'''
    return a ** 2 * (3 ** 0.5) / 4

Pp = p_tr_rown(3 ** 0.25)

print(Pp)

def p_prst(a, b):
    return a * b

Psb = p_prst(5, 4)
print(Psb)


def p_gran_praw_troj(a, b):
    return 2 * p_tr_rown(a) + 3 * p_prst(a, b)

Pg= p_gran_praw_troj(7, 4)
print(Pg)



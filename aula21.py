def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')


contador(0, 10, 2)
help(contador)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(2, 1, 5)
r2 = somar(3, 4)
r3 = somar(2)

print(f'Os resultados foram {r1}, {r2} e {r3}')



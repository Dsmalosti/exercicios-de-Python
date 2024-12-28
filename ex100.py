from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('Pronto!')


def somaPar(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f'Somando os valores pares da lista {lista}, temos {par}')



numeros = list()
sorteia(numeros)
somaPar(numeros)


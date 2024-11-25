from random import randint
from time import sleep
computador = randint(0,5)
print(20 * '-=-')
print('Vou pensar em um número entre 0 e 5. Tente acertar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador > 5:
    print('o numero escolhido é entre 0 e 5. Tente novamente')
    jogador = int(input('Em qual número eu pensei? '))
    print('PROCESSANDO...')
    sleep(3)
    if jogador == computador:
        print('Boa, voce acertou')
    else:
        print('Ganhei, o numero era {} e voce pensou em {}'.format(computador, jogador))
else:
    if jogador == computador:
        print('Boa, voce acertou')
    else:
        print('Ganhei, o numero era {} e voce pensou em {}'.format(computador, jogador))

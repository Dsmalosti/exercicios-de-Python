from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jog]))
print('-=' * 11)
if computador == 0: # Computador jogou PEDRA
    if jog == 0: # jogador jogou PEDRA
        print('Empate!')
    elif jog == 1: # jogador jogou PAPEL
        print('Jogador ganhou!')
    elif jog == 2: # jogador jogou TESOURA
        print('Computador gannhou!')
    else:
        print('Jogada inválida!')
elif computador == 1: # Computador jogou PAPEL
    if jog == 0: # jogador jogou PEDRA
        print('Computador gahou!')
    elif jog == 1: # jogador jogou PAPEL
        print('Empate!')
    elif jog == 2: # jogador jogou TESOURA
        print('Jogador ganhou!')
    else:
        print('Jogada inválida!')
elif computador == 2: # Computador jogou TESOURA
    if jog == 0: # jogador jogou PEDRA
        print('Jogador ganhou!')
    elif jog == 1: # jogador jogou PAPEL
        print('Computador ganhou!')
    elif jog == 2: # jogador jogou TESOURA
        print('Empate!')
    else:
        print('Jogada inválida!')

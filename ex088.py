from random import randint
jogo = []
jogos = []
print('-' * 30)
print('      JOGA NA MEGA SENA          ')
print('-' * 30)
qntdjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {qntdjogos} JOGOS -=-=-=')
for c in range(1, qntdjogos + 1):
    num = 0
    while num < 6:
        jogo.append(randint(0, 60))
        num += 1
    jogos.append(jogo[:])
    jogo.clear()
for i, l in enumerate(jogos):
    print(f'jogo {i + 1}: {l}')



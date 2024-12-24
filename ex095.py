jogador = dict()
gols = list()
time = list()
while True:
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, jogador['partidas'] + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['total'] = sum(gols)
    jogador['gols'] = gols[:]
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Erro! Por favor digite somente S ou N: ')).strip().upper()[0]
        if continuar == 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-" * 60)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    elif busca>= len(time):
        print('Jogador não encontrado, por favor digite o numero de um jogador da lista. ')
    else:
        print(f'  -- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 60)
print('<< Volte sempre >>')


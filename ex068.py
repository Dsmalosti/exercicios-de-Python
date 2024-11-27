from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 30)
    computador = randint(0,10)
    soma = valor + computador
    resultado = 1
    if soma % 2 == 0:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU PAR')
        resultado += 1
    else:
        print(f'Você jogou {valor} e o computador {computador}. Total de {soma} DEU ÍMPAR')
    print('-' * 30)
    if escolha == 'P':
        if resultado == 2:
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        elif resultado == 1:
            print('VOCÊ PERDEU!')
            break
    if escolha == 'I':
        if resultado == 1:
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        elif resultado == 2:
            print('VOCÊ PERDEU!')
            break
    print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')



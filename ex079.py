valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor digitado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar!')
    pergunta =''
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if pergunta == 'SN':
            break
    if pergunta == 'N':
        break
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 0:
        par.append(lista[pos])
    else:
        impar.append(lista[pos])
    pos += 1
par.sort()
impar.sort()
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
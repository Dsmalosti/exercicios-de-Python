dados = []
lista = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
        if resp == 'SN':
            break
    if resp == 'N':
        break
print('=-' * 30)
print(lista)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'o maior peso foi de {maior}, peso de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}',end='')
print()
print(f'o menor peso foi de {menor}, peso de ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}',end='')

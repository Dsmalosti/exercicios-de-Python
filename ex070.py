print('-' * 30)
print('{:^30}'.format('Loja de Taubaté'))
print('-' * 30)
total = prodmais1000 = maisbarato = cont = 0
nomemaisbarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if preco > 1000:
        prodmais1000 += 1
    if cont == 0 or preco < maisbarato:
        maisbarato = preco
        nomemaisbarato = nome
    cont += 1
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {prodmais1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${maisbarato:.2f}')


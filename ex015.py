dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valor = (dias * 60) + (km * 0.15)
print('o valor a ser pago é R${:.2f}'.format(valor))
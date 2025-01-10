from funcoesdoex109 import dobro, metade, aumento, moeda
n = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(n)} é {moeda(metade(n, True))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n, True))}')
print(f'Aumentando 10%, temos {moeda(aumento(n, True))}')

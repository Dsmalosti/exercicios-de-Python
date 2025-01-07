from funcoesdoex108 import dobro, metade, aumento, moeda
n = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(n)} é {moeda(metade(n))}')
print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
print(f'Aumentando 10%, temos {moeda(aumento(n))}')

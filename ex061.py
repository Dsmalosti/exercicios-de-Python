print('Gerador de PA')
print('-=' * 10)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
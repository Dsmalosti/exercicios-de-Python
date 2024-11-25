i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('passo: '))
for c in range(i, f + 1, p):
    print(c)

s = 0
for soma in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
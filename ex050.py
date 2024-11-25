soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Você informou {} pares e a soma de todos os números é {}'.format(cont, soma))

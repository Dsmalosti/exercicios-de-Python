parar = False
cont = soma = maior = menor = 0
while parar != True:
    num = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if opcao == 'N':
        parar = True
        soma += num
    elif opcao == 'S':
        soma += num
    else:
        opcao = str(input('Opção inválida, quer continuar? [S/N] ')).strip().upper()[0]
        if opcao == 'N':
            parar = True
            soma += num
        elif opcao == 'S':
            soma += num
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
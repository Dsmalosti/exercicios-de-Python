valor = float(input('Qual é o valor: R$ '))
print('''[ 1 ] - à vista dinheiro/pix: 10% de desconto
[ 2 ] - à vista no cartão: 5% de desconto
[ 3 ] - em até 2x no cartão: preço normal
[ 4 ] - 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
elif opcao == 4:
    total = valor + (valor * 20 / 100)
else:
    total = 0
    print('Opção incorreta! escolha outra forma de pagamento.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
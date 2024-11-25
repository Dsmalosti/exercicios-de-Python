salario = float(input('Qual é o sálario do funcionário? R$'))
aumento = (salario * 15 / 100) + salario
print('Um funcionário que recebe R${:.2f} com 15% de aumento passará a receber R${:.2f}'.format(salario, aumento))
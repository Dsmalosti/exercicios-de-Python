salario = float(input('Qual é o salario do funcionario? '))
if salario <= 1250.00:
    aumento = salario + salario * 15 / 100
else:
    aumento = salario + salario * 10 / 100
print('O seu salario atual é R${:.2f} e com o aumento fica R${:.2f}'.format(salario, aumento))
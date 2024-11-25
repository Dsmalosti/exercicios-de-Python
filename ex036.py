vc = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
ano = int(input('Quantos anos de financiamento? '))
mensal = vc / (12 * ano)
limite = salario * 30 / 100
if mensal > limite:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo negado!'.format(vc, ano, mensal))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo concedido!'.format(vc, ano, mensal))
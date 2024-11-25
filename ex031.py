distancia = float(input('Digita a distancia em Km da sua viagem: '))
if distancia <= 200:
    valor = 0.50 * distancia
else:
    valor = 0.45 * distancia
print('O valor da passagem de {:.2f}Km é igual R${:.2f}'.format(distancia, valor))
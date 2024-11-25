while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor * c}')
    print('-' * 30)
    cont = 1
print('Programa tabuada encerrado. Volte sempre!')
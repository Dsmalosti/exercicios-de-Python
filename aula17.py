valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chueguei ao final da lista.')

#Criar copia da lista
a = [3, 8, 9, 6]
b = a[:]
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')

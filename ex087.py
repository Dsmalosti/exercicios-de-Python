matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somapar = somacol = maiorvalor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacol += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorvalor:
                maiorvalor = matriz[l][c]
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somacol}')
print(f'O maior valor da segunda linha é {maiorvalor}')
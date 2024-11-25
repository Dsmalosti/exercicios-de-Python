from time import sleep
num = int(input('Digite um número: '))
print('O computador irá retornar se {} é par ou ímpar'.format(num))
print('PROCESSANDO...')
sleep(2)
resultado = num % 2
if resultado == 0:
    print('{} é par!'.format(num))
else:
    print('{} é ímpar'.format(num))

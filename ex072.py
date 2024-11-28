from time import sleep
cont = ('cero', 'uno', 'dos', 'tres', 'cuatro',
        'cinco', 'seis', 'siete', 'ocho', 'nueve',
        'diez', 'once', 'doce', 'trece', 'catorce',
        'quince', 'dieciséis', 'diecisiete', 'dieciocho',
        'diecinueve', 'veinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente! ', end='')
    print(f'Você digitou o número {cont[num]}')
    sleep(2)
    resp = ' '
    while resp not in 'N':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
          quit()
        elif resp == 'S':
            print('Vamos novamente!')
            break
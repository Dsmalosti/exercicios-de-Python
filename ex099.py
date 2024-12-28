from time import sleep
def maior(*args):
    mv = 0
    print('Analisando os valores passados...')
    for i, v in enumerate(args):
        if v > mv:
            mv = v
        print(v, end=' ')
        sleep(1)
    print(f'Foram informados {len(args)} valores ao todo.')
    print(f'O maior valor informado foi {mv}.')
    print('-=' * 30)


print('-=' * 30)
maior(3, 4, 5)
maior(8, 2, 3, 2, 1, 4, 2, 1)
maior()
maior(2, 1, 5, 2, 1)
from time import sleep
def lin():
    print('-=' * 20)

def contagem(i, f, p):

    if p < 0:
        p *= 1
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f - 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')


lin()
contagem(1, 10, 1)
lin()
contagem(10, 0, -2)
lin()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)

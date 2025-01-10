
def metade(num = 0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)

def dobro(num = 0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)

def aumento(num = 0, taxa = 0, formato=False):
    porc = (num * taxa) / 100
    res = num + porc
    return res if formato is False else moeda(res)

def reducao(num = 0, taxa = 0, formato=False):
    porc = (num * taxa) / 100
    res = num - porc
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.',',')

def resumo(num = 0, taxaAumento = 0, taxaReducao = 0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{taxaAumento}% de aumento: \t{aumento(num, taxaAumento, True)}')
    print(f'{taxaAumento}% de redução: \t{reducao(num, taxaReducao, True)}')
    print('-' * 30)

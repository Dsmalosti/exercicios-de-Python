
def metade(num = 0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)

def dobro(num = 0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)

def aumento(num = 0, formato=False):
    dez = (num * 10) / 100
    res = num + dez
    return res if formato is False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco}'.replace('.',',')

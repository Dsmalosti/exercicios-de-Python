def metade(num = 0):
    metadedenum = num / 2
    return metadedenum

def dobro(num = 0):
    dobrodenum = num * 2
    return dobrodenum

def aumento(num = 0):
    dez = (num * 10) / 100
    aumentodenum = num + dez
    return aumentodenum

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>1.2f}'.replace('.',',')

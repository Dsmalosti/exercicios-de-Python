from utilidades import dado
from utilidades import moeda

n = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(n, 10, 20)
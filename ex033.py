pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))
#verificando qual e o menor
menor = pri
if seg < pri and seg < ter:
    menor = seg
if ter < pri and ter < seg:
    menor = ter
#verificando qual e o maior
maior = pri
if seg > pri and seg > ter:
    maior = seg
if ter > pri and ter > seg:
    maior = ter
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
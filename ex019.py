from random import choice
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')
lista = [pri, seg, ter, qua]
escolhido = choice(lista)
print('O aluno sorteado foi {}'.format(escolhido))

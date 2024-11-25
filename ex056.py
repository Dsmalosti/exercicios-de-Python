count = 0
totidade = 0
maisidade = 0
idademenos = 0
for c in range(1, 5):
    count += 1
    print('-'*4,'{}º PESSOA'.format(count),'-'*4)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    totidade += idade
    sexo = input('Sexo [M/F]: ').strip().upper()
    if sexo == 'M':
        if idade > maisidade:
            maisidade = idade
            maisnome = nome
    if sexo == 'F':
        if idade < 20:
            idademenos += 1
media = totidade / 4
print('A média de idade é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisidade, maisnome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(idademenos))

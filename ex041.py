from datetime import date
ano = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade > 9 and idade <= 14:
    print('Classificação: Infantil')
elif idade > 14 and idade <= 19:
    print('Classificação: Júnior')
elif idade > 19 and idade <= 25:
    print('Classificação: Senior')
elif idade > 25:
    print('Classificação: Master')

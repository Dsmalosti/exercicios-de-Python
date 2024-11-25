from datetime import date
sexo = input('Qual é seu sexo? ')
if sexo == 'feminino':
    print('No Brasil as mulheres não precisam se alistar!!!')
else:
    ano = int(input('Ano de nascimento: '))
    data = date.today().year
    idade = data - ano
    tempo = idade - 18
    anodealista = date.today().year + abs(tempo)
    anoquealisto = date.today().year - abs(tempo)
    if tempo < 0:
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, data))
        print('Ainda faltam {} anos para o alistamento.'.format(abs(tempo)))
        print('Seu alistamento será em {}.'.format(anodealista))
    elif tempo == 0:
        print('Quem nasceu em {} tem 18 anos em {}\nVocê tem que se alistar imediatamente!'.format(ano,data))
    else:
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, data))
        print('Você já deveria ter se alistado há {} anos.'.format(tempo))
        print('Seu alistamento foi em {}.'.format(anoquealisto))
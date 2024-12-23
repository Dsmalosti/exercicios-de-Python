from datetime import date
pessoa = {'Nome': str(input('Nome: ')),
          'Idade': date.today().year - int(input('Ano de nascimento: ')),
          'Ctps': int(input('Carteira de trabalho (0 não tem): '))}
if pessoa['Ctps'] != 0:
     pessoa['Contratação'] = int(input('Ano de contratação: '))
     pessoa['Salário'] = float(input('Salário: R$'))
     pessoa['aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - date.today().year)
print('-=' * 30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')

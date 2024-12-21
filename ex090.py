aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
print('-=' * 30)
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
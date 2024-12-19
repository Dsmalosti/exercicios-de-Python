alunos = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('1º nota: ')))
    aluno.append(float(input('2° nota: ')))
    alunos.append(aluno[:])
    aluno.clear()
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if pergunta == 'SN':
            break
    if pergunta == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
pos = media = 0
while pos < len(alunos):
    media = (alunos[pos][1] + alunos[pos][2]) / 2
    print(f'{pos:<4}{alunos[pos][0]:<10}{media:>8.1f}')
    pos += 1
while True:
    print('-' * 35)
    mostrarNotas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrarNotas == 999:
        print('Finalizando...')
        break
    if mostrarNotas <= len(alunos) - 1:
        print(f'Notas de {alunos[mostrarNotas][0]} são {alunos[mostrarNotas][1:]}')
print('<<< Volte sempre >>>')



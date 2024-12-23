dados = list()
pessoa = dict()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Por favor, digite novamente: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Erro! Responda apenas com S OU N ')).strip().upper()[0]
        if continuar == 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
for c in range(0, len(dados)):
    soma += dados[c]['idade']
media = soma / len(dados)
print(f'B) A média de idades é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in dados:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('     << ENCERRADO >>')
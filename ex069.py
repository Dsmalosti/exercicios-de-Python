maior = homem = mulher = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
         break
print(f'Total de pessoas coma mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
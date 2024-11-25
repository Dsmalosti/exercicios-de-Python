n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media <= 5:
    print('Reprovado!')
elif media >= 7:
    print('Aprovado!')
else:
    print('Recuperação!')

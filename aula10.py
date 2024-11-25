n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m <= 6.0:
    print('Voce está abaixo da média')
else:
    print('Parabens, voce esta acima da média')
print('Sua média é {:.1f}'.format(m))
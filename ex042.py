n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Segundo segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n3:
    print('Os segmentos acima podem formar um triangulo')
    if n1 == n2 == n3:
        print('Equilatero!')
    elif n1 != n2 != n3 != n1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima não podem formar um triangulo')

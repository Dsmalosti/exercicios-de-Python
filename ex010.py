l = float(input('Qual é a largura da sua parede?'))
a = float(input('Qual é a altura da sua parede'))
area = l * a
litro = area / 2
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f} m.'.format(l, a, area))
print('Para pintar sua parede, voce precisará de {}l de tinta.'.format(litro))

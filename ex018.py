import math
angulo = float(input('Digite o angulo que voce deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, sen))
print('O angulo de {} tem cosseno de {:.2f}'.format(angulo, cos))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tan))
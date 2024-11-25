vel = float(input('Qua a velocidade do seu carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Multado! Voce excedeu o limite permitido que é de 80Km/h \nVoce deve pagar uma multa de R${:.2f}!'
          '\nTenha um bom dia. Dirija com segurança'.format(multa))
else:
    print('Tenha um bom dia. Dirija com segurança')
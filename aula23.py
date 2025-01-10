try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possivel dividir um número por zero!')
except (KeyboardInterrupt):
    print('O usúario preferiu não informar os dados')
else:
    print(f'O resultado é {div:.1f}')
finally:
    print('Volte sempre. obrigado!')
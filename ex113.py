def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usúario preferiu não digitar esse número.')
            return 0
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Usúario preferiu não digitar esse número.')
            return 0
        else:
            return num


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
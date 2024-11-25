from datetime import date
anohoje = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    if ano - anohoje >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade.'.format(maior,menor))




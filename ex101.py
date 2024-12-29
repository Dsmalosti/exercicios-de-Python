def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))



from time import sleep
pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
sair = False
total = 0
while not sair:
    sleep(2)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa''')
    opçao = int(input('>>>>> Qual a sua opção: '))
    if opçao == 5:
        sair = True
        print('Finalizando...')
        print('=-=' * 11)
        sleep(2)
    elif opçao == 1:
        total = pri + seg
        print('O resultado de {} + {} é {}'.format(pri, seg, total))
        print('=-=' * 11)
    elif opçao == 2:
        total = pri * seg
        print('O resultado de {} X {} é {}'.format(pri, seg, total))
        print('=-=' * 11)
    elif opçao == 3:
        if pri > seg:
            print('Entre {} e {} o maior é {}'.format(pri, seg, pri))
        elif pri < seg:
            print('Entre {} e {} o maior é {}'.format(pri, seg, seg))
        else:
            print('Os dois números são iguais')
        print('=-=' * 11)
    elif opçao == 4:
        print('Informe os números novamente')
        pri = int(input('Primeiro valor: '))
        seg = int(input('Segundo valor: '))
        print('=-=' * 11)
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa! Volte sempre!!!')
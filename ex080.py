lista = []
for c in range(0, 5):
    v = int(input("Digite um valor: "))
    if c == 0 or v > lista[-1]:
        print("Adicionado ao final da lista...")
        lista.append(v)
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


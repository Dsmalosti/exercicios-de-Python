teste = list()
teste.append('Gustavo')
teste.append(22)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 23
galera.append(teste[:])
print(galera)

pessoas = [['Ana', 45], ['José', 76], ['Felipe', 34], ['mauricio', 23]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')
pessoas = {'nome': 'Diogo',
           'idade': 20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Jao'
pessoas['peso'] = 89.4
for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
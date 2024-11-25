nome = input('Qual é seu nome? ').strip()
if nome.upper() == 'DIOGO':
    print('Que nome lindo!')
elif nome.upper() == 'JOAO' or nome.upper() == 'MATEUS' or nome.upper() == 'MARIA':
    print('Seu nome é muito comum')
elif nome.upper() in 'PAULA ANA JULIA':
    print('Que nome feiooo')
else:
    print('Nao gosto do seu nome')
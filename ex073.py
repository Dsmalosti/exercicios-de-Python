times = ('Botafogo', 'Palmeiras', 'Internacional', 'Fortaleza', 'Flamengo',
         'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians', 'Atlético-MG',
         'Vasco', 'Vitória', 'Juventude', 'Grêmio', 'Athletico-PR',
         'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atlético-GO')
print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Palmeiras está na {times.index("Palmeiras") + 1}º posição')
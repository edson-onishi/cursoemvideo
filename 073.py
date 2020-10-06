'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem 
de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')

print(f'Os 5 primeiros são: {times[0:5]} ')
print(30*'-=')

print(f'Os últimos 4 colocados: {times[-4:]} ')
print(30*'-=')

print(f'Times em ordem alfabética: {sorted(times)} ')
print(30*'-=')

print(f'Em que posição está o time da Chapecoense: {times.index("Chapecoense")}')

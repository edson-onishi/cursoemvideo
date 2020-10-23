'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogadores = dict()
partidas = list()
jogadores['nome'] = str(input('Digite um nome: '))
jogos = int(input('Quantas partidas jogadas: '))

for i in range(0,jogos):
    partidas.append(int(input(f' Quantos gols na partida {i + 1}: ')))
jogadores['gols'] = partidas[:]   
jogadores['total'] = sum(partidas)

print(f' O jogador {jogadores["nome"]} jogou {len(jogadores["gols"])} partidas')
for k,v in enumerate(jogadores['gols']):
    print(f'No {k+1}º jogo fez {v} gols')
print(f'Total de gols {jogadores["total"]}')    

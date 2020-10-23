''' Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
jogadores = dict()
partidas = list()
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Digite um nome: '))
    jogos = int(input('Quantas partidas jogadas: '))
    partidas.clear()
    for i in range(0,jogos):
        partidas.append(int(input(f' Quantos gols na partida {i + 1}: ')))
    jogadores['gols'] = partidas[:]   
    jogadores['total'] = sum(partidas)
    time.append(jogadores.copy())
    while True:
        r = str(input("Deseja continuar [S/N] : ")).strip().upper()[0]
        if r in 'SN':
            break  
        print('Resposta invalida! Responda com S ou N ')
    if r == 'N':
        break

print('{"id":<4}', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()    

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')  
    print()    

while True:
    id = int(input('Qual jogar mostrar? (999 para parar)'))
    if id == 999:
        break
    if id >= len(time):
        print(f'Id invalido! digite novamente: ')
    else:
        print(f'  -- levantamento do jogador {time[id]["nome"]}')
        for i, g in enumerate(time[id]["nome"]):
            print(f'        no jogo {i+1} fez {g} gols')
    print('-' * 30)        
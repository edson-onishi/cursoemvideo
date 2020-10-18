''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos 
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

import random
lista = list()
jogos = list()
qtdjogos = int(input("Quantos jogos: "))
total = 1
while total <= qtdjogos:
    cont = 0
    while True:
        n = random.randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()    
    total +=1
for i, l in enumerate(jogos):  
    print(f'{i+1}º jogo: {l}')

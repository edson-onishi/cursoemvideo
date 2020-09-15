'''Crie um programa que faca o computado jogar jokepo com voce.'''

import random

n = random.randrange(1,3)
jogador = int(input("Escolha:\n 1 - Tesoura\n 2 - Pedra\n 3 - Papel\n Digite sua jogada: "))

if n == jogador:
    print("Voce escolheu: {} e o Computador: {}\n Empate!".format(jogador,n))
elif n == 1 and jogador == 3 or n == 2 and jogador == 1 or n == 3 and jogador == 2:
    print("Voce escolheu: {} e o Computador: {}\n Voce Perdeu!".format(jogador,n))
else:
    print("Voce escolheu: {} e o Computador: {}\n Voce Ganhou!".format(jogador,n))    

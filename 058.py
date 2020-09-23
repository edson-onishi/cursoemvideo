'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

import random
tentativa = 1
n = random.randrange(0,10)
print(n)
print("Sou seu computador... acabei de pensar em um numero entre 0 e 10.")
n1 = int(input("Qual seu palpite ? "))
while n != n1:
    n1 = int(input("Voce errou, tente outro numero: "))
    tentativa +=1
print("Computador pensou no numero: {},voce acertou na {} tentativa".format(n,tentativa))  
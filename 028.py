'''Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5
 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
 o programa devera escrever venceu ou perdeu.
 '''

import random

n = random.randrange(0,5)
print("Descubra o numero escolhido de 0 a 5")
n1 = int(input("Digite um numero: "))

if n == n1:
    print("Venceu")
else:
    print("perdeu, numero escolhido foi: {}".format(n))    

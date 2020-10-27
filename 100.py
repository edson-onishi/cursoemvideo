'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre 
todos os valores pares sorteados pela função anterior.'''

import random

def sorteia(l):
    for n in range(0,5):
        l.append(random.randint(0,10))
    
def somaPar(l):
    soma = 0
    for valor in l:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {l}, temos {soma}')        
      
numeros = list()
sorteia(numeros)
somaPar(numeros)
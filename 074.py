'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

n = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))

print(f'Numeros sorteados: {n}\nMenor numero: {sorted(n)[0]}\nMaior numero: {sorted(n)[-1]} ')
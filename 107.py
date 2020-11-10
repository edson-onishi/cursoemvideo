'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from ex107 import moeda

n = float(input('Digite um valor: '))

print(f'Aumentando {10}% de {n} temos R${moeda.aumentar(n,10)}')
print(f'Diminuindo {10}% de {n} temmos R${moeda.diminuir(n,10)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'A metade de R${n} é R${moeda.metade(n)}')

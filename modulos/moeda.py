'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(n):
    return  n + (n * 10/100)
    

def diminuir(n):
    return n - (n * 10/100)
    

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

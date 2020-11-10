'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(n, taxa, formato = False):
    r =  n + (n * taxa/100)
    return r if formato is False else moeda(r)
    

def diminuir(n, taxa,formato = False):
    r = n - (n * taxa/100)
    return r if formato is False else moeda(r)

def dobro(n,formato = False):
    r = n * 2
    return r if formato is False else moeda(r)


def metade(n,formato = False):
    r = n / 2
    return r if formato is False else moeda(r)

def moeda(n):
    return f'{n:8.2f}'.replace('.',',')   

def resumo(n,taxa,d):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preco Analisado: \t{moeda(n)}\nDobro do preco: \t{dobro(n, True)}\nMetade do Preco: \t{metade(n,True)}\n{taxa}% de aumento: \t{aumentar(n,taxa,True)}\n{d}% de reducao: \t{diminuir(n,d,True)}')
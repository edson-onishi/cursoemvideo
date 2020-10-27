'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*n):
    m = []
    for i in n:
        m.append(i)
    print(f'Foram informados {len(m)} valores\nO maior valor informado foi: {max(m)} ')

maior(2,3,4,5)    
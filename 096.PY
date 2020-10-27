'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''

def area(largura,comprimento):
    a = largura * comprimento
    print(f'área = {a}m². ')


largura = float(input('Digite a altura em metro: '))
comprimento = float(input('Digite a comprimento em metro: '))

area(largura,comprimento) 

'''Crie um programa que leia um numero inteiro e mostre na tela se ele e impar ou par'''
n = int(input("Digite um numero inteiro: "))

if n%2 == 0:
    print("O numero {} é par".format(n))    
else:
    print("O numero {} é impar".format(n))        
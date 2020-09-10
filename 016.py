'''Crie um programa  que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira'''

from math import trunc
n = float(input("Digite um valor: "))
print("Valor digitado: {} e sua porcao inteira: {} ".format(n,trunc(n)))
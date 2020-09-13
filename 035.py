'''Desenvolva um programa que leia o comprimento de 3 retas 
e diga ao usuario se ela podem ou nao formar um triangulo'''

a = float(input("Digite Primeiro numero: "))
b = float(input("Digite Segundo numero: "))
c = float(input("Digite Terceiro numero: "))

if a < b + c and b < a + c and  c < a + b:
    print("Os elementos {} {} {} formam um Triangulo".format(a,b,c))
else:
    print("Os elementos {} {} {} nao formam um Triangulo".format(a,b,c))    
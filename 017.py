'''Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, 
calcule e mostre o comprimento da hipotenusa.'''
import math
b = float(input("Digite valor do Cateto Oposto: "))
c = float(input("Digite valor do Cateto Adjacente: "))

a = math.sqrt(pow(b,2) + pow(c,2))

print("Valor de Hipotenusa e: {:.2f} cm".format(a))


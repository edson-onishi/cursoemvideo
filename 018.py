'''faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, 
cosseno e tangente desse angulo'''

from math import cos, sin, tan, radians
a = int(input("Digite valor de angulo: "))

print("O valor de Seno e : {:.2f} e o valor de cosseno: {:.2f} e tangente {:.2f} do angulo {:.2f} ".format(sin(radians(a)), cos(radians(a)), tan(radians(a)), a))



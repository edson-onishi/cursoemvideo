'''Faca um programa que leia um numero de 0 a 9999 e mostre no tela cada um dos digitos separados.
ex:
Numero digitado 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

n = int(input('Digite numero de 0 a 9999: '))

print("Numero digitado: {}\n Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}".format(n,n//1%10,n//10%10,n//100%10,n//1000%10))
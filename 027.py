'''Faca um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o ultimo nome separadamente.'''

n = input('Digite nome completo: ').split()

print("Primeiro nome: {} \n Ultimo nome: {} ".format(n[0],n[-1]))
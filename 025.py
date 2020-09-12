'''Crie um programa que leia o nome de uma pessooa e diga se ela tem "SILVA" no nome.'''

n = str(input('Digite nome completo: ')).strip()

print("Tem Silva no nome? {} ".format('silva' in n.lower()))
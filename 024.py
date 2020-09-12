'''Crie um programa que leia o nome de uma cidade  e diga se ela começa ou nao com o nome "SANTO".'''

n = str(input('Digite nome de uma cidade: ')).strip

print(n[:5].lower() == 'santo')


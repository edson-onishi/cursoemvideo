'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
 e o menor valor digitado e as suas respectivas posições na lista.'''

n = list()
for cont in range(0,5):
    n.append(int(input('Digite um valor: ')))

print(f'Voce digitou os valores: {n}')

print(f'O maior valor foi {max(n)} nas posições: ', end='')
for i, v in enumerate(n):
    if v == max(n):
        print(f'{i}...', end='')

print(f'\nO menor valor foi {min(n)} nas posições: ', end='')
for i, v in enumerate(n):
    if v == min(n):
        print(f'{i}...', end='')
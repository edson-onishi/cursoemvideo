'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
 separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

n = [[],[]]
for i in range(0,7):
    num = (int(input('Digite um valor: ')))
    if num % 2 ==0:
        n[0].append(num)
    else:
        n[1].append(num)     
print(f'Valores Impares: {sorted(n[1])}\nValores Pares: {sorted(n[0])}')            
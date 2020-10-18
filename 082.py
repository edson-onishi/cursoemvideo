'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três 
listas geradas.'''
numeros = list()
impares = list()
pares = list()
while True:
    n = (int(input('Digite um valor: ')))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)    

    r = str(input('Conntinuar [s/n]'))
    if r in 'Nn':
        break    
numeros.sort()    
print(f'Numeros digitados: {numeros} Pares: {pares} Impares: {impares}')    


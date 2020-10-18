'''Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:       
A) Quantos números foram digitados.                                                                     
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numeros = list()
while True:
    n = (int(input('Digite um valor: ')))
    numeros.append(n)

    r = str(input('Conntinuar [s/n]'))
    if r in 'Nn':
        break    
numeros.sort(reverse = True)    
print(f'{len(numeros)} Numeros digitados: {numeros}')    

if 5 in numeros:
    print('Numero 5 foi digitado!')
else:
    print('numero 5 nao foi digitado')    
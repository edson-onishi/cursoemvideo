'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:    
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                                                                   
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
maior = list()
ma = me = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('peso: '))) 
    
    if len(maior) == 0:
        ma = me = pessoas[1]
    else:
        if pessoas[1] > ma:
            ma = pessoas[1]
        if pessoas[1] < me:
            me = pessoas[1]  
    maior.append(pessoas[:])              
    pessoas.clear()

    r = str(input("Deseja continuar [S/N] : ")).strip().upper()[0]
    if r =='N':
        break 
print(f' {len(maior):.0f} Pessoas cadastradas\nMaior peso foi {ma}')

print(f'Pessoas mais pessadas: ', end='')
for p in maior:
    if p[1] == ma:
        print(f'{p[0]}', end='')

print(f'Pessoas mais leves: ', end='')
for p in maior:
    if p[1] == me:
        print(f'{p[0]}', end='')        
      
    


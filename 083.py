'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
 
n = input('Digite uma expressão: ')
a = 0
b = 0
for i in n:
    if i == '(':
        a =+ 1
    elif i == ')':
        b =+ 1    
if b == a:
    print('expressão fechada')
else:
    print('expressão Aberta')    
     

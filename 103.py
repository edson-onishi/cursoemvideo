'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e 
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido 
informado corretamente.'''

def ficha(n='desconhecido', g=0):    
    print(f'O jogador {n} fez {g} gol(s)')


n  = str(input('Nome do jogador: ')) 
g = str(input('Numero de Gols: '))

if n == '':
    n = 'desconhecido'
if g =='' or g.isalpha():
    g = '0' 
if n.strip() == '':
    ficha(g = g)    
else:
    ficha(n,g)    

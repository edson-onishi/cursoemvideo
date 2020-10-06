'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Edson', 'Henrique', 'souza', 'Onishi')

for p in palavras:
    print(f'\n{p.upper()} temos: ', end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
'''Faca um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".

Em que posicao ela aparece a primeira vez.

Em que posicao ela aparece a ultima vez.'''

n = str(input('Digite uma frase: ')).strip().lower()



print("Quantas vezes aparece a letra 'A': {}\n Primeira posicao que ela aparece: {} \n Ultima posicao que ela aparece: {}".format(n.count('a'),n.find('a')+1,n.rfind('a')+1))
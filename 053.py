'''Crie um programa que leia uma frase qualquer e diga se ela e um polindromo, desconsiderando os espacos.'''
f = str(input("Digite uma Frase: ")).strip().lower()
p = f.split()
j = ''.join(p)
inve =''
for c in range(len(f)-1,-1,-1):
    inve += j[c]
if inve == j:
    print("A frase: {} {} Polindromo".format(j,inve))
else: 
    print("A frase: {} {} nao e um polindromo".format(j,inve))
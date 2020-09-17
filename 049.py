'''Refaca o desafio 009, mostrando a tabiada de um numero que o usuario 
escolher, so que agora utilizando um laco for.'''

n = int(input("Digite um numero: "))

for i in range(0,11):
    print("{}x{} = {}".format(n, i, n*i))
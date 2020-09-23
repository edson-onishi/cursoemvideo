'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

p = int(input("Digite primeiro termo: "))
r = int(input("Razao: "))
termo = p
c = 1
while c <= 10:
    print("{}".format(termo), end=' > ')
    termo += r
    c += 1



 

'''Desenvolva um programa que leia o primeiro termo e a razao de um pa 
no final, mostre os 10 primeiros termos dessa progressao.'''

p = int(input("Digite primeiro termo: "))
r = int(input("Razao: "))
decimo = p + (10 - 1) * r
for c in range(p, decimo, r):
    print("{}".format(c), end=' > ')
print('FIM!')    
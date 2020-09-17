'''Faca um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.'''

p = 0
m = 1000
for i in range(1,5):
    n = float(input("Digite o peso: "))
    if n > p:
        p = n
    if n < m:
        m = n
print(" O maior peso {} e o menor peso {}".format(p,m))        


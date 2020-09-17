'''Desenvolva um programa que leia seis numeros inteiros e mostre a soma
 apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o.'''
soma = 0
for i in range(1,7):
    n = int(input("Digite um numero: "))
    if n % 2 ==0:
        soma = soma + n
print("Soma dos valores soma {}".format(soma))        
'''Faca um programa que leia 3 numeros e mostre qual e o maior e qual e o menor'''

a = float(input("Digite Primeiro numero: "))
b = float(input("Digite Segundo numero: "))
c = float(input("Digite Terceiro numero: "))

menor = a 

if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print("Maior numero digitado: {}\n Menor numero digitado:{} ".format(maior,menor))    
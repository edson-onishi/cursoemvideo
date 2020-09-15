'''Escreva um programa que leia dois numeros inteiros e compare-os  mostrando na tela uma mensagem:
- O primeiro valor e maior
- O segundo valor e maior
- Nao existe valor maior, os dois sao iguais'''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a > b:
    print("Primeiro valor e Maior")
elif a == b: 
    print("Nao existe valor maior, os dois sao iguais")   
else:
    print("O segundo valor e maior")

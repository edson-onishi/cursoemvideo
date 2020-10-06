'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

a = int(input("Digite um numro: "))
b = int(input("Digite um numro: "))
c = int(input("Digite um numro: "))
d = int(input("Digite um numro: "))
n = (a,b,c,d)

print(f"Numero 9 apareceu: {n.count(9)} vezes")
if 3 in n:
    print(f'O primeiro valor 3 digitado foi na posição {n.index(3)+1}')
else:
    print('Nao foi digitado o valor 3')    

print('Os valores pares digitados foram: ', end='')
for numero in n:
    if numero % 2 == 0:
        print(numero, end=" ")
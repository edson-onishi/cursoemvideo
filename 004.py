'''faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
e todas as informacoes possiveis sobre ela'''

n = input("Digite alguma coisa: ")

print("Essa variavel e do tipo {} \n ele é numerico: {} " .format(type(n), n.isalnum()))

if n.isalpha != False:
    print("Este caracter é alfabetico")
elif n.isalnum != True: 
    print("Este caracter é numerico")
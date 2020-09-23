'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''


cont = soma = res = n = 0

while res != 2:
    n = float(input("Digite um valor: "))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n        
    media = soma / cont
    res = int(input("Continuar? 1 - sim  \n2 - nao \n: "))
print("voce digitou {} numeros  e a media deles: {} ".format(cont,media))   
print("O maior valor foi {} e oo menor foi {}".format(maior,menor))
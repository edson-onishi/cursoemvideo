'''Crie um programa que leia dois valores e mostre um menu na tela'''

a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))

n = 0

while  n != 5:
    n = int(input(" [ 1 ] Somar\n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Novos números\n [ 5 ] Sair\n Digite a opcao: "))
    if n == 1:
        print(" A Soma dos dois valores {} ".format(a+b))
    elif n == 2:
        print(" A Multiplicao dos dois valores {} ".format(a*b))
    elif n ==3:
        if a > b:
            print("{} e maior que {} ".format(a,b))    
        elif a == b :
            print("{} e igual o numero {} ".format(a,b))   
        else:
            print("{} e maior que {} ".format(b,a)) 
    elif n == 4:
        a = float(input("Digite um numero: "))
        b = float(input("Digite um numero: "))
print("Fim")     

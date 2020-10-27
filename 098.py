'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada'''


def contador():   
    
    print('contagem de 1 até 10, de 1 em 1')
    for i in range(0,10,1):
        print(f'{i}', end=' ')
    print()    
    print('contagem de 10 até 0, de 2 em 2 ')    
    i = 10
    for i in range(10,0,-2):
       print(f'{i}', end=' ') 
    print()      
    inicio = int(input("Digite o inicio: "))    
    fim = int(input("Digite o fim: "))
    passo = int(input("Digite o passo: "))
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1        

    if inicio < fim:
        i = inicio
        while i <= fim:
            print(f'{i}', end=' ')
            i += passo
        print('fim')    
    else:
        i = inicio
        while i >= fim:
            print(f'{i}', end=' ')
            i -= passo 

contador()




'''Escreva um programa que leia um numero inteiro qualquer e peca para o usuario 
escolher qual sera a base de conversao:
1 - Binario
2 - octal
3 - hexadecimal'''

n = int(input("Digite um numero interiro: "))
escolha = int(input("Converter para: \n 1 - Binario \n 2 - Ocatal \n 3 - Hexadecimal \n digite o numero: "))

if escolha == 1:
    print("{} convertido para Binario {}".format(n,bin(n)))
elif escolha == 2:
    print("{} convertido para ocatal {}".format(n,oct(n)))    
elif escolha == 3:
    print("{} convertido para hexadecimal {}".format(n,hex(n)))    
else:
    print("opcao invalida")    
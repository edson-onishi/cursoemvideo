inteiro = int(input("Digite um numero inteiro: "))#Recebe valores: 7, -4, 0 e 897
print(type(inteiro))

pontoFluante = float(input("Digite um numro Real: "))#Recebe valores: 4.3, 00.32, -123.32 e 7.0
print(type(pontoFluante))

booleano = bool(True) #Recebe valores: True ou False
print(type(booleano))

string = str(input("digite um numero ou uma palavra: "))#Recebe valores: numericos ou letras dentro de aspas simples ou dupla
print(type(string))



'''Tipos de Print'''

soma = inteiro + pontoFluante
print("A soma entre inteiro e Real", soma)

print("soma de inteiro e real" , inteiro + pontoFluante)

print("Subtracao de inteiro com real {}".format(inteiro-pontoFluante))#colchete sera substituido pela variavel dentro do format


'''Teste de Tipos'''
print(inteiro.isnumeric())

algo = input("Digite alguma coisa: ")

print(algo.isalnum)
'''Faca um program que calcule a soma entre todos os numeros impares
 que sao multiplos de tres e que se encontram no intervalo de 1 ate 500.'''
soma = 0
for i in range(1,501,2):
    if i % 3 ==0:
        soma = soma + i
print(" A soma de todos os valores: {} ".format(soma))        
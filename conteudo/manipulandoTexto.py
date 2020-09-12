'''Manipulando texto'''

frase = "  Curso em Video Python   "

#Slice

print(frase[9])

print(frase[9:13])#pega do 9 ate 13 mas ele exclui o 13

print(frase[9:21])

print(frase[9:21:2])# Start, Stop and Step

print(frase[:5])#quando nao coloca Start ele comaça pelo 0

print(frase[15:])#tem o start e vai ate o final

print(frase[9::3])#Inicia no 9 ate o final pulando 3 em 3

print(frase[::2])#pulando dois em dois

#Analise de String

print(len(frase))

print(frase.count('o'))#contar quantos 'o' tem na frase

print(frase.count('o',0,13))#usando slice 

print(frase.find('deo'))# mostra a posicao que inicia 'deo'

print(frase.find('android'))# retorna -1, quando nao existe o que esta procurando

print('Curso' in frase)#operador para saber da existencia de algo dentro do objeto, retornando true or false

#Transformacao

print(frase.replace('Python',"Android"))#subtitui a palavra Python pela android

print(frase.upper())#coloca tudo em maiuscula

print(frase.lower())# coloca tudo em minusculo 

print(frase.capitalize())# deixa uma String com o primeiro elemento em maiusculo e o resto minusculo

print(frase.title())#Deixa em maiusculo a primeira letra de todas as palavras dentro da string

print(frase.strip())#remove todos os espaços no começo e no final +

print(frase.rstrip())# remove apenas do lado direito

print(frase.lstrip())#remove apenas do lado esquerdo

#Divisao 

separada = frase.split()#gera uma lista com todas as palavras separadas

print(separada)

#juncao

print('-'.join(separada))




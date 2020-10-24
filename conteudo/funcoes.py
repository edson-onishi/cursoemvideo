'''vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem
 ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python
  e como utilizá-lo com parâmetros simples e múltiplos.'''

def linha():
    print('-' * 30)


linha()
print('   CURSO EM VIDEO   ')
linha()
print('   APRENDA PYTHON   ')
linha()

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem('oi, como vai voce?')


def soma(a,b):
    s = a + b
    print(s)

soma(2,4)    


soma(b=1,a=2)

#empacotar 
def contador(*n):
    print(n)

contador(2,3,4,5,6,7,8)    
contador(2)

def contador1(*n):
    for valor in n:
        print(valor, end=' ')
    print('Fiim')

contador1(2,3,4,5)        


def contador2(*n):
    tam = len(n)
    print(f'Recebi os valores{n} e sao ao todo {tam} numeros')

contador2(2,3,4,5,6)    


def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
valores = [2,4,5,6,7]
dobra(valores)
print(valores)

def soma1(* valores):
    s = 0
    for n in valores:
        s += n
    print(f'A soma dos valores é igual: {s}')    

soma1(5,2)    
soma1(2,4,5,6,7,89)
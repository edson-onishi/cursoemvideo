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

#empacotar recebe varios valores
def contador(*n):
    print(n)

contador(2,3,4,5,6,7,8)    
contador(2)
print('=' * 50)
def contador1(*n):
    for valor in n:
        print(valor, end=' ')
    print('Fiim')

contador1(2,3,4,5)        

print('=' * 50)
def contador2(*n):
    tam = len(n)
    print(f'Recebi os valores{n} e sao ao todo {tam} numeros')

contador2(2,3,4,5,6)    

print('=' * 50)
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
valores = [2,4,5,6,7]
dobra(valores)
print(valores)

print('=' * 50)
def soma1(* valores):
    s = 0
    for n in valores:
        s += n
    print(f'A soma dos valores é igual: {s}')    

soma1(5,2)    
soma1(2,4,5,6,7,89)

#help(print)#mostra o docstrings( manual da funcao)


#help(soma1)
print('=' * 50)
def soma2(a,b,c=0):
    """
    faz a soma de tres valores e mostra o resultadoi na tela
    a = o primeiro valor
    b = o segundo valor
    c = parametro opcional que recebe valor 0 caso nao receba o terceiro valor
    funcao criada por Edson Onishi
    """
    s = a+b+c
    print(f'A sina vale {s} ')
print('=' * 50)
def teste(b):
    #global a para usar o valor de a local como global
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale: {a}')
    print(f'B dentro vale: {b}')
    print(f'C dentro vale: {c}')  

a = 5
teste(a)
print(f'A fora vale: {a}')

# funcao com retorno, para retornar valor 

print('=' * 50)
def soma3(a=0,b=0,c=0):
    s = a + b + c
    return s
soma = soma3(2,3,4)
print(soma)
print(soma3(2,3,4))

print('=' * 50)
def fatorial(n = 1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()        

print(f'Os resultados sao {f1}, {f2} e {f3} ')

print('=' * 50)
def par (n=0):
    if n % 2 ==0:
        return True
    else:
        return False

n = int(input("Digite um nemro: "))
if par(n):
    print('par')
else:
    print("impar")         
print(par(n))

print('=' * 50)

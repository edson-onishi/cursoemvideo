'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a 
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo 
de cálculo do fatorial.'''

def fatorial(n = 1, processo=False):
    """
    Calcular o Fatorial de um numero
    :param n: o numero a ser calculado.
    :param processo: (opcional) mostrar o processo de calculo na conta ou nao.
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if processo == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')    
        f *= c
    return f

print(fatorial(5,True))    

help(fatorial)
        
  
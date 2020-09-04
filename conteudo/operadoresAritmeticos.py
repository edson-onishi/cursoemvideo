'''Operadores '''

print("Operador de adicao (+) usado entre 5 e 2 o resultado é: {}".format(5+2))

print("Operador de Subtracao (-) usado entre 5 e 2 o resultado é: {}".format(5-2))

print("Operador de Multiplicao (*) usado entre 5 e 2 o resultado é: {}".format(5*2))

print("Operador de Potencia (**) usado entre 5 e 2 o resultado é: {}".format(5**2))

print("Operador de Divisao (/) usado entre 5 e 2 o resultado é: {}".format(5/2))

print("Operador de Divisao inteira (//) usado entre 5 e 2 o resultado é: {}".format(5//2))

print("Operador de Resto da divisao (%) usado entre 5 e 2 o resultado é: {}".format(5%2))

'''Ordem de Precedencia'''

primeiro = 'parentese - ()'
segundo = 'potencia - **'
terceiro = 'neste caso resolve o operador que aparecer primeiro (*, /, // e %)'
quarto = '+ e -'


print(5 + 3 * 2)
print((5 + 3) * 2)


n1 = int(input("Digite um valor: " ))
n2 = int(input("DIgite outro valor: "))

s , m , d, di, e, a = n1 + n2, n1*n2, n1/n2, n1//n2, n1**n2, n1-n2

print("A soma e {}, o produto é {} e a divisão é {:.2f}".format(s,m,d))

print("Divisao inteira {} e potencia {}".format(di,e), end=' ')#(,end='') usado para nao quebrar a linha 

print("Subtracao e {}".format(a))

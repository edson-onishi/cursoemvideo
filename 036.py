'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o
 emprestimo sera negado.'''

valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu Salario: "))
tempo = int(input("Quantos anos de financiamento: "))

valorMensal = valorCasa/(tempo*12)

if valorMensal > (salario*30)/100:
    print("Emprestimo Negado")
else:
    print("Emprestimo Aprovado")    
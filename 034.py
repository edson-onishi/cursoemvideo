'''Escreva um program que pergunte o salario de um funcionario e calcule o valor do seu aument.
Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento e de 15%.'''

n = float(input("digite seu salario: "))

if n > 1250:
    print("Salario atual R$: {} com aumento de 10% R$: {}".format(n,n+(n*10)/100))
else:
    print("Salario atual R$: {} com aumento de 15% R$: {}".format(n,n+(n*15)/100))    
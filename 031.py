'''Desenvolva um programa que pergunte a distancia de uma viagem em km.
calcule o preco da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas.'''

n = int(input("Digite a distacia da viagem: "))

if n <= 200:
    print("Valor da passagem e R$: {} ".format(n*0.50))
else:
    print("Valor da passagem e R$: {} ".format(n*0.45))   
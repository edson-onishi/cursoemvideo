'''Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao servico militar.
- Se e a hora de se alistar.
- Se ja passou do tempo do alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

ano_atual = date.today().year
nascimento = int(input("Digite o ano do seu nascimento: "))

if (ano_atual - nascimento) < 18:
    print("nao esta no tempo de se alistar")
elif (ano_atual - nascimento) == 18:
    print("Esta no ano de se alistar")
else: 
    print("Passou do tempo de alistamento.")

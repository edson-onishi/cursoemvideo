'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
 a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input("Qual valor sacar: "))
total = valor
nota = 50 
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f"Total de {totalnota} cedulas de R${nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnota = 0
        if total == 0:
            break                     
'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo.
A multa vai custar R$7,00 por cada km acima do limite.'''

v = float(input("Digite a velocidade do carro: "))

if v > 80:
    print("Voce passou {:.0f}km acima do limite de velocidade, Multa de R$:{}".format((v - 80),(v - 80) * 7))
else:
    print("Voce esta no limite de velocidade")    

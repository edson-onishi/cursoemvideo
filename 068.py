'''aça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random
vi = 0
while True:
    pc = random.randrange(1,6)
    escolher = int(input("1 - Impar\n2 - Par\nDigite sua escolha:"))
    n = int(input("Digite um valor: "))
    soma = pc + n
    if escolher == 1:
        if soma % 2 == 1:
            print("Ganhou!")
            vi +=1
        else:
            print("Pedeu!")
            break
    elif escolher == 2:
        if soma % 2 == 0:
            print("Ganhou!")
            vi +=1
        else:
            print("Pedeu!")
            break  
    print("jogar novamente...")      
print(f"Fim de jogo! voce ganhou {vi} vezes")    


'''Crie um programa que leia o ano de nascimento de sete pessoas. 
no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.'''

from datetime import date
cont = 0
con1 = 0
ano_atual = date.today().year
for i in range(0,7):
    nascimento = int(input("Digite o ano do seu nascimento: "))
    if (ano_atual - nascimento) >= 18:
        cont += 1
    else:
        con1 += 1    
print("{} pessoas nao atingiram a maioridade e {}  ja sao maiores".format(con1,cont))
    

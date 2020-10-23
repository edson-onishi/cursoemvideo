'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e 
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
trabalhador = dict()

trabalhador['Nome'] = str(input('Digite um nome: '))
trabalhador['Idade'] = datetime.now().year - int(input('Digite ano de nascimento: '))  
trabalhador['Carteira de trabalho'] = int(input('Digite numero da carteira de trabalho (0 - nao tem): ')) 

if trabalhador['Carteira de trabalho'] != 0:
    trabalhador['Ano de Contratação'] = int(input("Digite ano de contratação: "))
    trabalhador['Salário'] = float(input("Digite salario: "))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Ano de Contratação'] + 35) - datetime.now().year)
for k, v in trabalhador.items():   
    print(f'{k}: {v}') 



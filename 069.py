'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

soma = m = f = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Qual seu sexo  [F/M] : ")).strip().upper()[0]
        if idade > 18:
            soma += 1
        if sexo == 'F' and idade < 20:
            f += 1
        if sexo =='M':
            m += 1  
    e = ' '        
    while e not in 'SN':
        e = str(input("Deseja continuar [S/N] : ")).strip().upper()[0]
    if e =='N':
        break 
print(f"{soma} Pessoas maiores de 18 anos\n{m} Homens cadastrados\n{f} Mulheres tem menos que 20 anos")  
   
  



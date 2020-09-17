'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
- A media de idade do grupo.
- Qual e o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.'''
soma = 0
maior = ''
menor = 0
for i in range(0,4):
    n = str(input("Digite nome: "))
    idade = int(input("Digite idade: "))
    sexo = int(input("1 - Feminimo\n 2 - Masculino"))
    soma = soma+idade
    if sexo == 2 and idade >= idade:
        idade = idade
        maior = n
    elif sexo == 1 and idade < 20:
        menor += 1    

print("A media do grupo {} {} e o mais velho dos homens {} Mulheres tem menos de 20 anos".format(soma/4, maior,menor))
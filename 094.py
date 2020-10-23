''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
mulheres = list()
pessoa = dict()
pessoas = list()
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Digite um nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo: [M/F] ")).upper()
        if pessoa['sexo'] == 'F':
            mulheres.append(pessoa['nome'])
        if pessoa['sexo'] in 'MF':
            break
        print('Opcao invalida, Digite novamente M ou F')
        
    pessoa['idade'] = int(input('Digite idade: '))
    media += pessoa['idade']
    pessoas.append(pessoa.copy()) 
    r = str(input("Deseja continuar [S/N] : ")).strip().upper()[0]
    if r =='N':
        break        

print(f'Quantas pessoas foram cadastradas: {len(pessoas)} ')
print(f'A média de idade: {media/len(pessoas):.1f}')
print(f'Uma lista com as mulheres: {mulheres}')
print(f'Uma lista de pessoas com idade acima da média: ',)

for p in pessoas:
    if p['idade'] >= media/len(pessoas):
        for k,v in p.items():
            print(f' {k} = {v} ', end='')
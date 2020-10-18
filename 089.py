'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = list()
while True:
    n = str(input("Digite um nome: "))
    nota1 = float(input("Digite primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = nota1 + nota2/2
    alunos.append([n, [nota1,nota2], media])
    r = str(input('Conntinuar [s/n]'))
    if r in 'Nn':
        break    
print(f'{"Matricula":<20}Nome Média')
print('-=' * 25)
for i, l in enumerate(alunos):  
    print(f'{i:<20} {l[0]:<20} {l[2]:<20}')

while True:
    r = str(input("Deseja ver nota individual[s/n]: "))
    if r in 'Nn':
        break 
    matricula = int(input("Digite numero da matricula do aluno: "))
    if matricula <= len(alunos):
        print(f'Aluno: {alunos[matricula][0]} obteve notas {alunos[matricula][1][0]} e {alunos[matricula][1][1]}')


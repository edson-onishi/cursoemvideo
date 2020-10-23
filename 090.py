'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input("Digite a media: "))

if aluno['media'] < 5: 
   aluno['situação'] = 'Reprovado'
elif aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Recuperacao'

for k, v in aluno.items():
    print(f' {k} é igual a {v} ')
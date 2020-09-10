'''o mesmo professor do desafio sortear a ordem de apresentacao de trabalhos
 dos alunos. faca um programa que leia o nome de quatro alunos e ,mostre a ordem sorteada'''

from random import shuffle

a = input("DIgite primeiro aluno: ")
b = input("DIgite segundo aluno: ")
c = input("DIgite terceiro aluno: ")
d = input("DIgite quarto aluno: ")
n = [a, b, c, d]
shuffle(n)
print("Ordem de apresentacao: {} ".format(n))

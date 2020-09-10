'''Um professor quer sortear uj dos seus quatros alunos para apagar o quadro
 faca um programq uqe ajude ele lendo o nome deles e escrevendo o nome do escolhido'''

from random import choice

a = input("DIgite primeiro aluno: ")
b = input("DIgite segundo aluno: ")
c = input("DIgite terceiro aluno: ")
d = input("DIgite quarto aluno: ")
n = [a, b, c, d]

print("Aluno escolhido foi: {} ".format(choice(n)))
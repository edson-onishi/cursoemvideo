'''Crie um program que leia duas notas de um aluno e calcule sua media, mostrando uma 
mensagem no final, de acordo com a media atingida:
- media abaixo de 5: reprovado
- Media entre 5 e 6.9: recuperacao
- Media 7 ou superior: aprovado'''

a = float(input("Digite sua primeira nota: "))
b = float(input("Digite sua segunda nota: "))

media = (a+b)/2

if media < 5: 
    print("Reprovado")
elif media >= 7:
    print("Aprovado")  
else:
    print("Recuperacao")      
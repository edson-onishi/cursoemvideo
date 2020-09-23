'''face um programa que leia o sexo de uma pessoa, mas so aceite os valores "m" ou "f" 
caso esteja errado, peca a digitacao novamente ate ter um valor correto.'''
s = str(input("Digite seu sexo [M/F] : ")).strip().lower()[0]
while s != 'm' and  s != 'f':
    s = str(input("Dados invalidos, Digite seu sexo [M/F] : ")).strip().lower()[0]
print("Sexo digitado: {} ".format(s))    
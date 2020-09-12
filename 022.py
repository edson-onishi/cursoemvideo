'''Crie um program que leia o nome completo de uma pessoa e mostre: 
O nome todo maiusculo, 
o nome todo em munusculo, 
Quantas letras ao todo sem considerar o espaco tem o primeiuro nome.'''

n = input('Digite nome completo: ')


print("Nome todo em maiusculo: {} \n Nome todo em minusculo: {} \n Total de letras sem espaco:{}\n Total de letras do primeiro nome: {}".format(n.upper(),n.lower(),len(n.replace(" ","")),len(n.split()[0])))
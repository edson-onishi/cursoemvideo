'''Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.'''

n = int(input("Digite preco do produto: "))

print("Valor do produto com 5% de desconto: {} ".format(n-(n*5)/100))
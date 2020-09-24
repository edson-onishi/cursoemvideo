'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''                


cont = to = qt = menor = 0
mn = ''

while True:
    n = str(input("Nome do produto: "))
    p = float(input("Preco do produto: "))
    to += p
    cont += 1 
    if p > 1000:
        qt += 1
    if cont == 1 or p < menor:
        menor = p
        mn = n  
    e = ' ' 
    while e not in 'SN':
        e = str(input("Deseja continuar [S/N] : ")).strip().upper()[0]
    if e =='N':
        break 
print(f"Total: {to}\n{qt} Produtos acima de R$: 1000\nO produto mais barato foi {mn} que custa R$ {menor}")    

'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

p = ('Arroz', 23.32, 'Feijao', 24.32, 'Macarrao', 4.1)

print("        LISTA DE PRECO")
for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos] : <30}', end='')
    else:
        print(f'R${p[pos] :>8}')    

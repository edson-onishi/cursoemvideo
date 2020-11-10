'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números 
como um valor monetário formatado.'''
from ex107 import moeda

n = float(input('Digite um valor: '))

print(f'Aumentando {10}% de R${moeda.moeda(n)} temos R${moeda.moeda(moeda.aumentar(n,10))}')
print(f'Diminuindo {10}% de R${moeda.moeda(n)} temos R${moeda.moeda(moeda.diminuir(n,10))}')
print(f'O dobro de R${n} é R${moeda.moeda(moeda.dobro(n))}')
print(f'A metade de R${moeda.moeda(n)} é R${moeda.moeda(moeda.metade(n))}')
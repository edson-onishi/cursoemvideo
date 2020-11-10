'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor  
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from ex107 import moeda

n = float(input('Digite um valor: '))

print(f'Aumentando {10}% de {n} temos R${moeda.aumentar(n,10,True)}')
print(f'Diminuindo {10}% de {n} temmos R${moeda.diminuir(n,10,True)}')
print(f'O dobro de R${n} é R${moeda.dobro(n,True)}')
print(f'A metade de R${n} é R${moeda.metade(n,True)}')
'''Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis 
compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(type(lanche))
print(lanche[2])
print(lanche[1:3])

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi muito.')    

for cont in range(0, len(lanche)):
    print(cont , end=' ')
print('FIM')    

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posicao {pos} ')
print('FIM')    

print(sorted(lanche))
print(lanche)

a = (2,5,4)
b = (5,8,1,2)
c = b + a
d = a + b
print(c)
print(d)

pessoa = ('Edson', 31, 'M', 94.22)
del(pessoa)
print(pessoa)
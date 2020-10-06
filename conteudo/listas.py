'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas 
que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.'''

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
print(num)

num.sort(reverse=True)
print(num)

num.sort()
print(num)

num.insert(2,0)
print(num)

num.pop(2)
print(num)

num.remove(2)
print(num)

valores = []
valores.append('Edson')
valores.append('Henrique')
valores.append('Souza')
valores.append('Onishi')

valores.remove('Henrique')# funcao remove, remove pelo conteudo
print(valores)

valores.insert(1,'Henrique')
print(valores)

valores.pop(1)#funcao pop remove o elemento pelo index
print(valores)

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v} ')
print('Cheguei no final da lista')    

'''n = list()
for cont in range(0,5):
    n.append(int(input('Digite um valor: ')))

for c, v in enumerate(n):
    print(f'Na posicao {c} encontrei o valor {v} ')
print('Cheguei no final da lista')      '''

a = [2, 3, 4, 7]
b = a# aqui fazemos uma ligacao e nao uma copia da lista
print(f'Lista A: {a}\nLista B: {b}\n')

b[2] = 8 # vemos aqui a ligacao ele muda o elemento nas duas lista 
print(f'Lista A: {a}\nLista B: {b}\n')

b = a[:]#assim fazemos uma copia de lista
print(f'Lista A: {a}\nLista B: {b}\n')

b[2] = 3 
print(f'Lista A: {a}\nLista B: {b}')


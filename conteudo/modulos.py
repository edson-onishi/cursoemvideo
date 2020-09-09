

'''import math #importa tudo que estiver dentro da biblioteca math
num = int(input("Digitre um numero: "))
raiz = math.sqrt(num)
print("A Raiz de {} é igual a {} ".format(num,raiz))'''


'''from math import sqrt #importa apenas a função sqrt dentro da biblioteca math
num = int(input("Digitre um numero: "))
raiz = sqrt(num)
print("A Raiz de {} é igual a {} ".format(num,raiz))'''


from math import sqrt, floor # utilizando virgula da pra importar quantas funcoes desejar.
num = int(input("Digitre um numero: "))
raiz = sqrt(num)
print("A Raiz de {} é igual a {} ".format(num,floor(raiz)))
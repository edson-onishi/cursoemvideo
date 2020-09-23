'''for c in range(1,6):
    print("Oi")
    print("Final")
print("FIM")    

for c in range(0,6):\
    print(c)
print("FIM")    

for c in range(6, 0, -1):
    print(c)
print("FIM")    

for c in range(1, 7, -2):
    print(c)
print("FIM")  

n = int(input("Digite um nuemro: "))
for c in range(0, n+1):
    print(c)
print("FIM")    

s = 0
for c in range(0,4):
    n = int(input('DIgite um valor: '))
    s += n
print("O somatorio de todos os valores foi {} ".format(s))    '''

'''WHILE'''

c = 1
while c <10:
    print(c)
    c += 1
print('FIM!')    

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1    
print("Voce digitou {} numeros pares e {} numeros impares".format(par,impar))    

r = 's'
while r == 's':
    n = int(input("DIgite um valor: "))
    r = str(input("Deseja continuar [S/N] ")).lower()
print("FIM!!!")    
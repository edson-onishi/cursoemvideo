'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

p = int(input("Digite primeiro termo: "))
r = int(input("Razao: "))
termo = p
c = 1
total = 0
mais= 10
while mais != 0:
    total = total + mais
    while c <= total:
        print("{}".format(termo), end=' > ')
        termo += r
        c += 1
    print('Pausa')    
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
print("Fim")    
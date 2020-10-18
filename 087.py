'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = cont = 0
for i in range(0,3):
    for j in range(0,3):
        n =  (int(input('Digite um valor: ')))   
        matriz[i][j] = (n)  
        if n % 2 ==0:
            par += n
                
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]} ')    
print(f'A Soma de todos os valores pares: {par}\nA soma dos valores da terceira coluna: {matriz[0][2]+matriz[1][2]+matriz[2][2]}\nO maior valor da segunda linha: {max(matriz[1])}') 

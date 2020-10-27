'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(n):
    while True:
        n = input("Digite um numero: ")
        if n.isnumeric():
            break
        else:
            False
            print('Erro!')    
    return n            

n = leiaInt('Digite um nuemro: ')
print(f'O numero digitado foi: {n}')
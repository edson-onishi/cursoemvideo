'''Condicionais'''

n = str(input('Qual seu nome: ')).strip().capitalize()

if n == 'Edson':#condicao simples,sem o else.
    print('Belo nome')
else:#condicao composta
    print('seu nome e normal')    
print('Bom dia, {} '.format(n))    

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

if m >= 6:
    print("Sua media foi boa")
else:
    print('sua media foi ruim')    

    
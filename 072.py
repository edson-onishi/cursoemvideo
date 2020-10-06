'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

n = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',  'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Deseseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um numero (entre 0 e 20): '))
    if  0 <=  num <= 20:
        break
    print('Tente novamente!', end='')

print(f'Voce digitou o numero {n[num]} ')


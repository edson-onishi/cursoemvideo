'''try:
    a = int(input("numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except:
    print('Infelizmente tivemos um problema')'''


'''try:
    a = int(input("numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce  digitou.')   
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')         
else:
    print(f'O resultado é {r:.1f}')   
finally:
    print('volte sempre! muito obrigado') '''    




'''idade = int(18)
if (idade < 18):
    print("nao pode tirar habilitacvao")
if idade >= 18:
    print("pode ter habilitacao")    

texto = 'computacao'    
if len(texto) >= 10:
    print('texto com mais 10 caracteres')'''

def palindromo(palavra_1):
    palavra_1 = palavra_1.lower().strip().replace(' ','')
    if palavra_1 == palavra_1[::-1]:
        print ('True')
    else:
        print('False')    
def main():
    palavra_1 = str(input('Digite uma palavra: '))
    palindromo(palavra_1)
main()
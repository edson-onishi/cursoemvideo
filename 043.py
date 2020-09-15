'''Desenvolva um logica que leia o peso e a altura de uma pessoam calcule seu IMC 
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5 abaixo do Peso 
- Entre 18.5 e 25 peso ideal
- 25 ate 30 sobrepeso
- 30 ate 40 obesidade 
- acima de 40 Obesidade morbida'''

p = float(input("Digite seu peso: "))
a = float(input("digite sua altura: "))

imc = p/(a*a)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and  imc <= 25:
    print("Peso ideal")
elif imc > 25 and  imc <= 30:
    print("Sobrepeso") 
elif imc > 30 and  imc <= 40:
    print("Obesidade")  
else: 
    print("Obesidade Morbida")         
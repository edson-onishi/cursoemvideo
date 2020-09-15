'''A confederacao Nacional de natacao precisa de um programa que leia o ano de nascimento 
de um atleta e mostre sua categoria, de acordo com a idade:
- ate 9 anos : mirim
- ate 14 anos : Infantil
- ate 19 anos : Junior
- ate 25 anos : Senior
- acima : master'''

i = int(input("Dggite sua idade: "))

if i <= 9:
    print("Mirim")
elif i <= 14:
    print("Infantil")
elif i <= 19:
    print("Junior")    
elif i <= 25:
    print("Senior")     
else: 
    print("Master")    
n = str(input("qual seu nome: ")).strip().capitalize()
if n == 'Edson':
    print("Que nome bonito!")
elif n == 'Pedro' or n == 'Maria' or n == 'Paulo':
    print("Seu nome e bem popular no Brasil.")
elif n in 'Ana Claudia Jessica Juliana':
    print("Belo nome Feminino")
else:
    print("Seu nome e bem normal.")    
print("Tenha um bom dia, {}!".format(n))    
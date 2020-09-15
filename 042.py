'''Refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
- Equilatero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaeno: Todos os lados diferentes'''

a = float(input("Digite Primeiro numero: "))
b = float(input("Digite Segundo numero: "))
c = float(input("Digite Terceiro numero: "))

if a < b + c and b < a + c and  c < a + b:
    if a == b and b == c:
        triangulo = "Equilatero"
    elif a == b or a ==c or b==c:
        triangulo = "Isoceles"    
    else:
        triangulo = 'Escaleno'    
    print("Os elementos {:.0f} {:.0f} {:.0f} formam um Triangulo {}".format(a,b,c,triangulo))
else:
    print("Os elementos {:.0f} {:.0f} {:.0f} nao formam um Triangulo".format(a,b,c))    
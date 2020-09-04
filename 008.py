"""Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros."""

n = float(input("Digite um valor: "))

print("Valor digitado em metros: {}m \n convertido em centimetros: {:.0f}cm e milimetros {:.0f}mm".format(n,n*100, n*1000 ))
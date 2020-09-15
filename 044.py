'''Elabore um program que calcule o valor a ser pago por um produto, considerando o seu preco normal
 e condicao de pagamento: 
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartao: 5% de desconto
- em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% de juros'''

p = float(input("Digite o preco do produto: "))

pagamento = str(input("Forma de Pagmento \n 1 - Dinheiro\n 2 - Cartao a vista\n 3 - Cartao 2x no cartao\n 4 - cartao 3x ou mais\n :"))



if pagamento == '1':
    print("Pagamento em Dinheiro com 10% de desconto {}".format(p - (p*10)/100))
elif pagamento == '2':
    print("Pagamento a vista no cartao com 5% de desconto {}".format(p - (p*5)/100))
elif pagamento == '3':  
    print("Pagamento em 2x vista no cartao {}".format(p))
elif pagamento =='4':
    print("Pagamento em 3x no cartao com 20% de desconto {}".format(p + (p*20)/100))

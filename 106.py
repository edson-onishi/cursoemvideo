'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''


def manual():
    while True:
        print('Manual do Python')
        n = str(input("Digite funcao ou biblioteca: "))
        if n.lower() in 'fim':
            break
        print('\033[1;31;43m')
        help(n)
        print('\033[m')

manual()    
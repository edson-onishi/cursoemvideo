'''\033[style text back m
0 - none
1 - bold
4 - underline
7 - negative
Cores text - 30 branco, 31 red, 32 green, 33 yellow, 34 blue, 35 purple, 36 aqua, 37 gray.
cores de background sao a mesma mas e do 40 ao 47
'''

print("\033[1;31;43mOla mundo!")

print("\033[2;31;42mOla mundo!\033[m")#para fechar o style tem qe usar o\033[m para parar a formatacao

print("Ola, {} Mundo{}".format('\033[32m','\033[m'))

Cores = {'limpa':'\033[m',
         'red': '\033[31m',
         'green': '\033[32m',
         'yellow': '\033[33m'}

print(" ola {}mundo{}".format(Cores['red'], Cores['limpa']))         
s = 'prova de python'

print(len(s))
'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
import random
from time import sleep
from operator import itemgetter
jogador = dict()
jogador['Edson'] = random.randint(1,6)
jogador['Henrique'] = random.randint(1,6)
jogador['Souza'] = random.randint(1,6)
jogador['Onishi'] = random.randint(1,6)

for k, v in sorted(jogador.items(), key=itemgetter(1), reverse=True):
    print(f' O jogador {k} tirou numero: {v} ')
    sleep(1)

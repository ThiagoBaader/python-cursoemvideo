"""
EXERCÍCIO 091: Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
ranking = list()
print('== #PARTIU JOGAR OS DADOS! ==')
print(f'{"Boa sorte à todos!":^29}')
sleep(0.9)
for c in range(1, 5):
    jogo[f'Jogador{c}'] = randint(1, 6)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.9)
print('-=' * 20)
print(f'    == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.9)

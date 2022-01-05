"""
EXERCÍCIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')

"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

print('\033[7;32;40m-=-\033[m' * 20)
print('\033[30mVou pensar em um número entre 0 e 5.Tente\033[m \033[4;30madivinhar...\033[m')
print('\033[7;33;40m-=-\033[m' * 20)
computador = randint(0, 5)
jogador = int(input('\033[30mEm que número pensei? \033[m'))
print('\033[30mPROCESSANDO...\033[m')
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[35mGANHEI! Eu pensei no número {} e não no {}.\033[m'.format(computador, jogador))

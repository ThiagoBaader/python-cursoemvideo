"""
EXERCÍCIO 088: Palpites Para a Mega Sena
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep
cadastro = []
jogos = []
n = 0
tot = 1
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, end=' ')
print(f'SORTEANDO {quantidade} JOGOS', end=' ')
print('-=' * 3)
while tot <= quantidade:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in cadastro:
            cadastro.append(n)
            cont += 1
        if cont >= 6:
            break
    cadastro.sort()
    jogos.append(cadastro[:])
    cadastro.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

"""
EXERCÍCIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de: {total}.', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    print('-' * 30)
    if escolha == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU.')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('VOCÊ PERDEU.')
            break
    print('Vamos jogar novamente...')
    print('-' * 30)
print('=-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes.')

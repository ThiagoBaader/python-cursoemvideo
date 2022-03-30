"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep
def maior(* n):
    print('-=' * 20)
    print('Analisando os valores informados...')
    for valor in n:
        print(f'{valor}', end=' ')
        sleep(0.3)
    print(f'\nForam informados {len(n)} valores ao todo.')
    if len(n) > 0:
        print(f'O maior valor informado foi {max(n)}.')
    else:
        print(f'O maior valor informado foi 0.')


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior( )

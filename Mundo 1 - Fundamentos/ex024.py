"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

cidade = str(input('\033[7;30;47mEm que cidade você nasceu? \033[m')).upper().replace('-', ' ').strip().split()
print('SANTO' == cidade[0])

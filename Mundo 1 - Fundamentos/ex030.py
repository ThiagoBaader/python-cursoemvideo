"""
EXERCÍCIO 030: Par ou Ímpar?
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

n = int(input('\033[35mMe diga um número qualquer: \033[m'))
if (n % 2 == 0):
    print('\033[35mO número {} é PAR!\033[m'.format(n))
else:
    print('\033[35mO número {} é ÍMPAR!\033[m'.format(n))

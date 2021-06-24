"""
EXERCÍCIO 019: Sorteando um Item na Lista
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice
p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
lista = [p, s, t, q]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

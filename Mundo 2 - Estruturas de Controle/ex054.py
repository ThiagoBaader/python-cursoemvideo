"""
EXERCÍCIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
atual = date.today().year
tot = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if atual - ano >= 21:
        tot += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(tot))
print('E também tivemos {} pessoas menores de idade.'.format(c - tot))

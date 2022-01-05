"""
EXERCÍCIO 055: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

maior = 0
menor = 9999
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {} kgs.'.format(maior))
print('O menor peso foi {} kgs'.format(menor))

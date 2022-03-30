"""
EXERCÍCIO 078: Maior e Menor Valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end=' ')
for c, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{c}', end='... ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{c}', end='... ')

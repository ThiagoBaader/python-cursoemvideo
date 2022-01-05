"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
q = int(input('Quantos termos você quer mostrar? '))
print('~' * 30)
c = 1
termo = 0
ultimo = 0
penultimo = 1
while c <= q:
    print('{}'.format(termo), end=' > ')
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    c += 1
print('FIM')
print('~' * 30)

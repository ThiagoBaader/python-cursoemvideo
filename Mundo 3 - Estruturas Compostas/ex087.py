"""
EXERCÍCIO 087: Mais Sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Difite um valor para {[l, c]}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        coluna += matriz[l][2]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma de valores da terceira coluna é {coluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

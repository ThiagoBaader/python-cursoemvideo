"""
EXERCÍCIO 042: Analisando Triângulos v2.0
Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos podem formar um triângulo', end=' ')
    if n1 != n2 != n3 != n1:
        print('escaleno.')
    elif n1 == n2 == n3:
        print('equilátero.')
    else:
        print('isósceles.')
else:
    print('Os segmentos não podem formar um triângulo.')

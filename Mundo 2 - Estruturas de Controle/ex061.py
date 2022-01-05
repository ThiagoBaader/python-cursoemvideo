"""
EXERCÍCIO 061: Progressão Aritmética v2.0
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

print('Gerador de PA')
print('-=' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print('{}'.format(t), end=' > ')
    t += r
    c += 1
print('FIM')

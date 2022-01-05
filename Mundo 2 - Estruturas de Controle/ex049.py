"""
EXERCÍCIO 049: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""

c = 0
n = int(input('Digite um número para ver sua tabuada: ' ))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (n * c)))
    c += 1

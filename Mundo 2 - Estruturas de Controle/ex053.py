"""
EXERCÍCIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""


frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
palindromo = frase[::-1]
print('O inverse de {} é {}.'.format(frase, palindromo))
if frase == palindromo:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

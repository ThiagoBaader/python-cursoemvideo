"""
EXERCÍCIO 018: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}.'.format(a, sin(radians(a))))
print('O ângulo de {:.1f} tem o COSENO de {:.2f}.'.format(a, cos(radians(a))))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}.'.format(a, tan(radians(a))))

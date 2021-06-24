"""
EXERCÍCIO 014: Conversor de Temperaturas
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""

tC = float(input('Informa e temperatura em ºC: '))
tF = (tC * 9/5) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(tC, tF))

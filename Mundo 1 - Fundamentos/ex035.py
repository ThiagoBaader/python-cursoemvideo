"""
EXERCÍCIO 035: Analisando Triângulo v1.0
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('\033[7;30mPrimeiro segmento: \033[m'))
n2 = float(input('\033[7;30mSegundo segmento: \033[m'))
n3 = float(input('\033[7;30mTerceiro segmento: \033[m'))

if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print('\033[1;30;42mOs segmentos acima podem formar um triângulo!\033[m')
else:
    print('\033[1;30;41mOs segmentos acima NÃO podem formar um triângulo!\033[m')

"""
EXERCÍCIO 033: Maior e Menor Valores
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('\033[0;30;44mPrimeiro valor: \033[m'))
n2 = int(input('\033[0;30;44mSegundo valor: \033[m'))
n3 = int(input('\033[0;30;44mTerceiro valor: \033[m'))
#Verificando menor número
menor = n1
if (n2 < n1) and (n2 < n3):
    menor = n2
if (n3 < n1) and (n3 < n2):
    menor = n3
#Verificando maior número
maior = n1
if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n1) and (n3 > n2):
    maior = n3
print('\033[0;30;44mO menor valor digitado foi {:.0f}\033[m'.format(menor))
print('\033[0;30;44mO maior valor digitado foi {:.0f}\033[m'.format(maior))

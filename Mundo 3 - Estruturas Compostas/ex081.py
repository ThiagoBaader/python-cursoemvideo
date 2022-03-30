"""
EXERCÍCIO 081: Extraindo Dados de uma Lista
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-=' * 50)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

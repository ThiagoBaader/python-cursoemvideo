"""
EXERCÍCIO 079: Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""

valores = list()
while True:
    continua = ''
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já digitado. Não vou adicionar.')
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores:', end=' ')
for c in valores:
    print(c, end=' ')

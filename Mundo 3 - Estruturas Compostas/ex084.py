"""
EXERCÍCIO 084: Lista Composta e Análise de Dados
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

cadastro = list()
dados = list()
maiorpeso = menorpeso = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(dados) == 0:
        maiorpeso = menorpeso = cadastro[1]
    else:
        if cadastro[1] > maiorpeso:
            maiorpeso = cadastro[1]
        if cadastro[1] < menorpeso:
            menorpeso = cadastro[1]
    dados.append(cadastro[:])
    cadastro.clear()
    continua = str(input('Quer continuar? (S/N) ')).strip().upper()[0]
    while continua not in 'SsNn':
        continua = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(dados):.0f} pessoas.')
print(f'O maior peso foi {maiorpeso}, peso de:', end=' ')
for pessoa in dados:
    if pessoa[1] == maiorpeso:
        print(f'{pessoa[0]}', end=' '),
print(f'\nO menor peso foi {menorpeso}, peso de:', end=' ')
for pessoa in dados:
    if pessoa[1] == menorpeso:
        print(f'{pessoa[0]}', end=' ')

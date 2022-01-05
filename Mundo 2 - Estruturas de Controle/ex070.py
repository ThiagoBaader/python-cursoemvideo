"""
EXERCÍCIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""

total = totmil = menor = cont = 0
menorprod = ' '
print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        menorprod = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'O total de compra foi R$ {total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00.')
print(f'O produto mais barato foi {menorprod} que custa R$ {menor:.2f}.')

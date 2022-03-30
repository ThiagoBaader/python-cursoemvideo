"""
EXERCÍCIO 082: Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.
"""

valores = []
pares = []
impares= []
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'A lista completa é: {valores}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')

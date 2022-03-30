"""
EXERCÍCIO 094: Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""

cadastro = dict()
dados = list()
totid = mediaid = 0

while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    cadastro['idade'] = int(input('Idade: '))
    totid += cadastro['idade']
    dados.append(cadastro.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if continua == 'N':
            break
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
mediaid = totid / len(dados)
print(f'B) A média de idade é {mediaid:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end=' ')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print(f'\nD) Lista de pessoas que estão acima da média: ')
for p in dados:
    if p['idade'] >= mediaid:
        print(f'    ', end = ' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
        print()
print('<< ENCERRADO >>')

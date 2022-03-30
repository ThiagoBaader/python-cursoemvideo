"""
EXERCÍCIO 089: Boletim com Listas Compostas
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""

cadastro = []
boletins = []
media = cont = aluno = 0
while True:
    nome = str(input('Nome: '))
    cadastro.append(nome)
    n1 = float(input('Nota 1: '))
    cadastro.append(n1)
    n2 = float(input('Nota 2: '))
    cadastro.append(n2)
    media = (n1 + n2) / 2
    cadastro.append(media)
    boletins.append(cadastro[:])
    cadastro.clear()
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-=' * 20)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 40)
for c in range(0, len(boletins)):
    print(f'{c:<4}', end=' ')
    print(f'{boletins[c][0]:<10}', end=' ')
    print(f'{boletins[c][3]:>8.1f}')
print('-' * 40)
while aluno != 999:
    aluno = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if aluno < len(boletins):
        print(f'As notas de {boletins[aluno][0]} são {boletins[aluno][1]} e {boletins[aluno][2]}')
        print('-' * 40)
    else:
        print(f'Número inválido. Você deve digitar um número entre 0 e {len(boletins) - 1}. Tente novamente!')
print('-' * 40)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

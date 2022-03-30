"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dados = dict()
partidas = list()
dados['nome'] = str(input('Nome do Jogador: '))
totpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, totpartidas):
    partidas.append(int(input((f'   Quantos gols na partida {c}? '))))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-=' * 40)
print(dados)
print('-=' * 40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {dados["nome"]} jogou {totpartidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')

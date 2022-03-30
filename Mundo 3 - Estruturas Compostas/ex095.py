"""
EXERCÍCIO 095: Aprimorando os Dicionários
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

cadastro = dict()
gols = list()
dados = list()
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome do Jogador: ')).capitalize()
    jogos = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    gols.clear()
    for c in range(0, jogos):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    dados.append(cadastro.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N!')
    if continua == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in cadastro.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for k, v in enumerate(dados):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 40)
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(dados):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[busca]["nome"]}')
        for i, g in enumerate(dados[busca]["gols"]):
            print(f'    - No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')

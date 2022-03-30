'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''

classificacao = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG',
'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-=' * 20)
print(f'Lista de times do Brasileirão 2019: {classificacao}')
print('-=' * 20)
print(f'Os 5 primeiros são: {classificacao[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {classificacao[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(classificacao)}')
print('-=' * 20)
print(f'A Chapecoense está na {classificacao.index("Chapecoense") + 1}ª posição.')

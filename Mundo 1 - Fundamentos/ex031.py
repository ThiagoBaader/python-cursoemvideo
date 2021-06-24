"""
EXERCÍCIO 031: Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

distancia = float(input('\033[4;33mQual é a distância da sua viagem? \033[m'))
print('\033[4;33mVocê está prestes a começar uma viagem de {:.2f} km.\033[m'.format(distancia))
if distancia <= 200:
    print('\033[4;33mE o preço da sua passagem será de R$ {:.2f}.\033[m'.format(distancia * 0.50))
else:
    print('\033[4;33mE o preço da sua passagem será de R$ {:.2f}.\033[m'.format(distancia * 0.45))

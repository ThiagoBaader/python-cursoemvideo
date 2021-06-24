"""
EXERCÍCIO 029: Radar Eletrônico
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

velocidade = float(input('\033[37mQual a velocidade atual do carro? \033[m'))
if velocidade > 80:
    print('\033[1;31mMULTADO!\033[m\033[31m Você excedeu o limite permitido que é de 80km/h\033[m')
    print('\033[31mVocê deve pagar uma multa de\033[m \033[1;31mR$ {:.2f}.\033[m'.format((velocidade - 80) * 7))
else:
    print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')

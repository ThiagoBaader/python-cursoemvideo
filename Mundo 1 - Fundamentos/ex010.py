"""

EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 3,27

"""

valor = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(valor, (valor/3.27)))

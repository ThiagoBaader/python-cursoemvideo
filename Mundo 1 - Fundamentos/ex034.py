"""
EXERCÍCIO 034: Aumentos Múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('\033[7;30mQual é o salário do funcionário? R$ '))
if salario >= 1250:
    nsalario = salario + (salario * 0.10)
else:
    nsalario = salario + (salario * 0.15)
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.\033[m'.format(salario, nsalario))

"""
EXERCÍCIO 036: Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
prazo = int(input('Quantos anos de financiamento: '))
parcela = valor / (prazo * 12)
limite = (salario * 0.30)
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format (valor, prazo, parcela))
if parcela <= limite:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

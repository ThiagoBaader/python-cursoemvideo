"""
EXERCÍCIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}'.format(' LOJAS GUANABARA '))
valor = int(input('Valor das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a forma de pagamento: '))
if opcao == 1:
    print('Sua compra de R$ {:.2f} com 10% de desconto vai custar R$ {:.2f} no final.'.format(valor, (valor - (valor * 0.10))))
elif opcao == 2:
    print('Sua compra de R$ {:.2f} com 5% de desconto vai custar R$ {:.2f} no final.'.format(valor, (valor - (valor * 0.05))))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(valor / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, (valor / parcelas)))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, (valor + (valor * 0.20))))
else:
    print('Opção de pagamento inválida, repita o processo!')

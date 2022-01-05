"""
EXERCÍCIO 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n1 < n2:
            print('O maior número é {}.'.format(n2))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segudo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')

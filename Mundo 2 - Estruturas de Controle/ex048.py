"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
cont = 0
for n in range(1, 501):
    if n % 2 == 1 and n % 3 == 0:
        #cont = cont + 1
        #soma = soma + n
        soma += n
        cont += 1
print('A soma de todos os {} números ímpares, múltiplos de 3, no intervalo de 1 a 500 é: {}'.format(cont, soma))

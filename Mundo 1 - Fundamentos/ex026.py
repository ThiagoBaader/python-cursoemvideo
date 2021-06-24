"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""

frase = str(input('\033[4;33mDigite uma frase: \033[m')).lower().strip()
print('\033[30mA letra\033[m \033[1;30mA\033[m \033[30mapareceu {} vezes na frase\033[m'.format(frase.count('a')))
print('\033[30mA primeira letra\033[m \033[1;30mA\033[m \033[30mapareceu na posição {}\033[m'.format(frase.find('a') + 1))
print('\033[30mA última letra\033[m \033[1;30mA\033[m \033[30mapareceu na posição {}\033[m'.format(frase.rfind('a') + 1))

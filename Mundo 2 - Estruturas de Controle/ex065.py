"""
EXERCÍCIO 065: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

n = 0
r = 'Ss'
cont = 0
soma = 0
menor = 0
maior = 0
while r in'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))

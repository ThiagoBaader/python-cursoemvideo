'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
b) quais foram os números pares
'''

n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores: {n}')
#análise do número 9:
if n.count(9) == 0:
    print('O número 9 não foi digitado nenhuma vez')
elif n.count(9) == 1:
    print(f'O valor 9 apareceu {n.count(9)} vez.')
else:
    print(f'O valor 9 apareceu {n.count(9)} vezes.')
#análise do número 3:
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')
#análise dos pares:
print(f'Os valores pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')

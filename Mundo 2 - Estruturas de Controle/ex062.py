"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0
Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

print('Gerador de PA')
print('-=' * 10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'. format(t), end=' -> ')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos vocês quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

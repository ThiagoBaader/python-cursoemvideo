"""
EXERCÍCIO 083: Validando Expressões Matemáticas
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

pa = pf = 0
expressao = input('Digite a expressão: ')
for caracteres in expressao:
    if '(' in expressao:
        pa += 1
    elif ')' in expressao:
        pf += 1
if pa > pf:
    print('Sua expressão está inválida!')
elif pa < pf:
    print('Sua expressão está inválida!')
else:
    print('Sua expressão está válida!')

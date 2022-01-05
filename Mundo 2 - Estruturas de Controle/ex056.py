"""
EXERCÍCIO 056: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

somaidade = 0
mediaidade = 0
maisvelho = 0
totm = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if sexo == 'M':
        if idade > maisvelho:
            maisvelho = idade
            nomevelho = nome
    if sexo == 'F' and idade < 20:
        totm += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho chama-se {} e tem {} anos.'.format(nomevelho, maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totm))

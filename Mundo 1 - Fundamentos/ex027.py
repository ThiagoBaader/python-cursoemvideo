"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

n = str(input('\033[32mDigite seu nome completo: \033[m')).strip()
nome = n.split()
print('\033[32mMuito prazer em te conhecer!\033[m')
print('\033[32mSeu primeiro nome é\033[m \033[4;32m{}\033[m'.format(nome[0]))
print('\033[32mSeu último nome é\033[m \033[4;32m{}\033[m'.format(nome[len(nome)-1]))

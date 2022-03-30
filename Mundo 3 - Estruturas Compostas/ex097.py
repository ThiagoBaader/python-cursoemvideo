"""Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.
Ex:
escreva("Olá, Mundo!")
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""

def cabeçalho(txt):
    tam = len(txt) + 4
    print(f'~' * tam)
    print(f'  {txt}')
    print(f'~' * tam)


# Programa Principal
cabeçalho('Gustavo Guanabara')
cabeçalho('Curso de Python no Youtube')
cabeçalho('CeV')

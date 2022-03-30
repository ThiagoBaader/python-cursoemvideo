"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
ex.:
n = leia_int("Digite um n")
"""

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033')
        if ok:
            break
    return valor


#Programa principal
print('-' * 30)
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')

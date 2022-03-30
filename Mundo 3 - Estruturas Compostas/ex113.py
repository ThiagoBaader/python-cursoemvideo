"""
Funções aprofundadas em Python
"""

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompidas pelo usuário!')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Digite um número real válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompidas pelo usuário!')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')

"""
Faça um minissistema que utilize o interactive help do Python
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará!.
OBS: use cores.
"""

rom time import sleep

cores = ('\033[m', #0 - sem cor
         '\033[0;30;47m', #1 - branco
         '\033[1;30;41m', #2 - vermelho
         '\033[1;30;42m', #3 - verde
         '\033[1;30;43m', #4 - amarelo
         '\033[1;30;44m', #5 - roxo
         '\033[1;30:45m', #6 - cinza
         '\033[1;30;46m', #7 - magenta
         )


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 5)
    print(cores[1], end='')
    help(comando)
    print(cores[0],end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)

#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)

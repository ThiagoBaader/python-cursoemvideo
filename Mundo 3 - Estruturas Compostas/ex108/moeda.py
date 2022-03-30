def aumentar(n=0, taxa=0):
    resultado = n + (n * (taxa/100))
    return resultado


def diminuir(n=0, taxa=0):
    resultado = n - (n * (taxa/100))
    return resultado


def metade(n=0):
    resultado = n / 2
    return resultado


def dobro(n=0):
    resultado = n * 2
    return resultado


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

def aumentar(n=0, taxa=0, format=False):
    resultado = n + (n * (taxa/100))
    return resultado if format is False else moeda(resultado)


def diminuir(n=0, taxa=0, format=False):
    resultado = n - (n * (taxa/100))
    return resultado if format is False else moeda(resultado)


def metade(n=0, format=False):
    resultado = n / 2
    return resultado if format is False else moeda(resultado)


def dobro(n=0, format=False):
    resultado = n * 2
    return resultado if format is False else moeda(resultado)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

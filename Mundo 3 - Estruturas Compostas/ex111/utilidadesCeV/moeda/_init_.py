def aumentar(n=0, taxa=0, format=False):
    '''
    ->Calcula o aumento para determinado preço, retornando um resultado com o sem formatação
    :param n: o preço que quer reajustar
    :param taxa: qual a porcentagem do aumento
    :param format: quer a saída formatada ou não
    :return: o valor reajustado, com ou sem formato
    '''
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


def titulo(msg):
    tam = len(msg) + 15
    print('-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)


def resumo(n=0, taxa=0, format=False):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(n,taxa, True)}')
    print(f'{taxa}% de redução: \t{diminuir(n, taxa, True)}')
    print('-' * (len('RESUMO DO VALOR') + 15))

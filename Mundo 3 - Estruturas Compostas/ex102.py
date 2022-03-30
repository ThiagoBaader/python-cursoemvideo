"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(n=1, show=False):
    """
    -> Cálcula o fatorial de um número.
    :param n: o número a ser calculado o fatorial
    :param show(opcional): True=Mostrar o cálculo / False=Não mostrar o cálculo
    :return: o resultado do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


#Programa principal
print(fatorial(5, show=True))
help(fatorial)

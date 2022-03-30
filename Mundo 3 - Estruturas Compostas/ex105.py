"""
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
quantidade de notas
a maior nota
a menor nota
a média da turma
a situação (opcional)
Adicione tambeem as docstrings da função
"""

def notas(*notas, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indica se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    info = dict()
    info['Total'] = len(notas)
    info['Maior'] = max(notas)
    info['Menor'] = min(notas)
    info['Media'] = sum(notas) / len(notas)
    if sit:
        if info['Media'] >= 7:
            info['Situacao'] = 'BOA'
        elif info['Media'] >= 5:
            info['Situacao'] = 'RAZOÁVEL'
        else:
            info['Situacao'] = 'RUIM'
    return info


#Programa principal
informacoes = notas(5.5, 2.5, 1.5, sit=True)
print(informacoes)
help(notas)

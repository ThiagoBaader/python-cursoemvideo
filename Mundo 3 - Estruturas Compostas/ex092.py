"""
EXERCÍCIO 092: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Nº da Carteira de Trabalho (0 se não tiver): '))
if dados['ctps'] == 0:
    print('Fim do programa!')
else:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
    print('-=' * 30)
    for k, v in dados.items():
            print(f'    - {k} tem o valor {v}')

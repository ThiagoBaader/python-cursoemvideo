"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from Ex112.utilidadesCeV import moeda
from Ex112.utilidadesCeV import dado

preco = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(preco, 35, 22)

"""
EXERCÍCIO 090: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

boletim = dict()
media = 0
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Media de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'aprovado'
elif 5 <= boletim['media'] <7:
    boletim['situacao'] = 'em recuperação'
else:
    boletim['situacao'] = 'reprovado'
print('-=' * 30)
#print(f'O nome do aluno é {boletim["nome"]}')
#print(f'A média de {boletim["nome"]} é {boletim["media"]}')
#print(f'A média de {boletim["nome"]} é {boletim["media"]}, portanto, o aluno está {boletim["situacao"]}
for k, v in boletim.items():
    print(f'- {k} é igual a {v}')

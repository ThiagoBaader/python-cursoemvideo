"""
EXERCÍCIO 043: Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Seu peso (kg): '))
altura = float(input('Sua altura (m): '))
IMC = peso / (altura ** 2)
print('Seu IMC é {:.1f}.'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= IMC < 25:
    print('Você está na faixa de peso ideal')
elif 25 <= IMC < 30:
    print('Você está com sobrepeso')
elif 30 <= IMC < 40:
    print('Você está com obesidade')
elif IMC >= 40:
    print('Você está com obesidade mórbida')

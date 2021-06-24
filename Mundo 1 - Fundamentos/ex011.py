"""
EXERCÍCIO 011: Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""

larg = float(input('Largura da parede (m): '))
alt = float(input('Altura da parede (m): '))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))

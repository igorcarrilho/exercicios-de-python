# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a
# quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de
# 2 metros quadrados
largura = float(input('Qual é a largura da parede?'))
altura = float(input('Qual é a altura da parede?'))
area = largura * altura
print('A parede tem {} x {} e a area é de {}m².'.format(largura, altura, area))
print('Serão necessários {} litros de tinta para pintar a parede'.format(area / 2))


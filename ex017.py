# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retêngulo.
# Calcule e mostre o comprimento da hipotenusa
# import math
from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
# print('O valor da hipotenusa será de {:.2f}'.format(hipotenusa))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')

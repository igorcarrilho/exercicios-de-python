# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente dese angulo
"""from math import hypot
co = float(input('Qual o cateto oposto?'))
ca = float(input('Qual o cateto adjacente?'))
hi = hypot(co, ca)
sen = co / hi
cos = ca / hi
tg = co / ca"""
# import math
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, seno))
ang2 = float(input('Digite o ângulo que você deseja:'))
cos = cos(radians(ang2))
print('O ângulo de {} tem o Coseno de {:.2f}'.format(ang2, cos))
ang3 = float(input('Digite o ângulo que você deseja'))
tg = tan(radians(ang3))
print(f'O ângulo de {ang3} tem a Tangente de {tg:.2f}')

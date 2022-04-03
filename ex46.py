# Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos de artifício, inde de 0 até 0,
# com uma pausa de 1 segundo entre eles
from time import sleep
print('CONTAGEM REGRESSIVA PARA OS FOGOS!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POW!')
print('FIM')

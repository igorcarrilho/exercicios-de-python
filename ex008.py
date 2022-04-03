# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros
medida = float(input('Digite um valor'))
k = medida * 0.001
h = medida * 0.1
d = medida * 0.1
dm = medida * 10
c = medida * 100
m = medida * 1000
print('A medida de {}m corresponde a:'.format(medida))
print('{}km, \n{}hm, \n{}dam'.format(k, h, d))
print('{}dm,\n{}cm, \n{}mm'.format(dm, d, c, m))

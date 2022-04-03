# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Quantos reais você tem? R$'))
dolar = float(real * 5.1)
print('Com R${} reais você pode comprar US${:.2f} dólares'.format(real, dolar))





# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0.15 por km rodado
km = float(input('Quantos Km o carro rodou?'))
dias = int(input('Quantos dias o carro foi alugado?'))
pagar = (dias * 60) + (km * 0.15)
print('O carro foi alugado por {} dias e rodou {} Km, portanto o valor a ser pago será de R${:.2f}'.format(dias, km, pagar))

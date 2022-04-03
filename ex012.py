# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input('Qual é o valor do produto? R$'))

desconto = produto - (produto * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% custará R${}'.format(produto, desconto))


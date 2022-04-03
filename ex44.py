# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento: a vista dinheir/cheque = 10% deconto, a vista cartão = 5% desconto, em até 2x = preço
# normal, 3x ou mais = 20% de juros
loja = ' CARRILHO STORE '
print(f'{loja:=^40}')
produto = int(input('Valor do produto? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual é a opção? '))
if pagamento == 1:
    desconto = produto - (produto * 10 / 100)
    print(f'Sua compra de R${produto:.2f} vai custar R${desconto:.2f} ao final com 10% de desconto.')
elif pagamento == 2:
    desconto = produto - (produto * 5 / 100)
    print(f'Sua compra de R${produto:.2f} vai custar R${desconto:.2f} ao final com 5% de desconto.')
elif pagamento == 3:
    pagamento = produto
    parcela = pagamento / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
    print(f'Sua compra de R${produto:.2f} vai custar R${pagamento:.2f}')
elif pagamento == 4:
    pagamento = produto + (produto * 20 / 100)
    parcelatotal = int(input('Quantas parcelas irá fazer? '))
    parcela = produto / parcelatotal
    print(f'Sua compra será parcelada em {parcelatotal}x de R${parcela:.2f}')
    print(f'Sua compra de R${produto:.2f} vai custar R${pagamento:.2f}')
else:
    print('Opção INVÁLIDA de pagamento. Tente novamente!')
    print(f'Sua compra de R${produto:.2f} irá custar R${produto:.2f} no final!')
print('FIM')

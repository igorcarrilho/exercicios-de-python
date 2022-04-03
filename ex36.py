# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30%
# do salário ou então o empréstimo será negado
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário mensal? R$'))
anos = int(input('Em quantos anos irá pagar a casa?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos:.2f} anos, a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo negado')
print('FIM')

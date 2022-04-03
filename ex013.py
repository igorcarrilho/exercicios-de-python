# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual é seu salário atual? R$'))
aumento = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${}, com 15% de aumento, passou a ganhar R${}'.format(salario, aumento))


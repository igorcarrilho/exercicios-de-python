# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários supeiores a 1250, calcule um aumento de 10%, Para inferiores ou iguais, aumento de 15%
salario = float(input('Qual é o seu salário? R$'))
if salario > 1250:
    novo = salario + salario * 0.10
    print(f'Seu salario sera de R${salario} e com o aumento foi para R${novo}')
if salario <= 1250:
    novo = salario + salario * 0.15
    print(f'Seu salário era de R${salario} e com o aumento foi para R${novo}')
print('FIM')

# Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Ímpar
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é Par')
else:
    print(f'O número {num} é Ímpar')
print('FIM')

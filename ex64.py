# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles.
n = cont = soma = 0
n = int(input('DIgite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('DIgite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles é de {soma}')
print('FIM')

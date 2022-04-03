# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o número 999, sendo a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre elas (desconsiderando o flag)
n = cont = s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores foi de {s}')
print('FIM')

# Faça um programa que mostre a tabuada de vários números, um de cada vez, cara cada valor digitado pelo usuário.
# O programa será intrerrompido quando o número solicitado for negativo
soma = cont = n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        print('Não é possível calcular a tabuada de um valor negativo!')
        break
    for c in range(1, 11):
        soma = soma + 1
        cont = cont + 1
        print(f'{n} x {cont} = {n * soma}')
    print('-' * 30)
print('FIM')

# Crie um programa que leia dois valores e mostre um Menu na tela: 1 - Somar, 2 - Multiplica,
# 3 - maior, 4 - novos números e 5 - sair do programa. Seu programa deverá realizar a operação solicitada
# em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('> Qual é a sua opção? < '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} multiplicado por {n2} é de {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre os números {n1} e {n2}, o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 14)
    sleep(2)
print('Fim do programa. Volter sempre!')
print('FIM')

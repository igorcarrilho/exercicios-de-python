# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor
n1 = int(input('Digite um número: '))
# ant = n1 - 1
# suc = n1 + 1
# print('Analisando o valor {}, o seu antecessor é o {} e o seu sucessor é o {}'.format(n1, ant, suc))
print('Analisando o valor {}, o seu antecessor é o {} e o seu sucessor é o {}'.format(n1, (n1 - 1), (n1 + 1)))

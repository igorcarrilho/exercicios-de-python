# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
n = str(input('Qual é o seu nome?')).strip()
nome = n.split()
print('Prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
print('FIM')

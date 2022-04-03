# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao total sem considerar espaços
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo:'))
dividido = nome.split()
print(nome)
print('Seu nome em letra maiúscula é {}'.format(nome.upper()))
print('Seu nome em letra minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], nome.find(' ')))
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')

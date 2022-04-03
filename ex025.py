# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome
nome = str(input('Digite seu nome: ')).strip()
# O in não é um método mas sim um operador que pode ser utilizado nesse caso
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

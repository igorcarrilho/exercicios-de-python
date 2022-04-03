# Faça um programa que leia algo pelo teclado e mostre na tela o seu tpo primitivo e todas as informações possíveis
# sobre ele
nome = input("DIgite algo")
print("O tipo primitivo desse valor é:", type(nome))
# Da para testar se mesmo o que for digitado for uma string pode ser um outro tipo
print("Só tem espaços?", nome.isspace())
print("É um número?", nome.isnumeric())
print("É alfabético?", nome.isalpha())
print("É alfanumérico?",nome.isalnum())
print("Está em maiúsculo?", nome.isupper())
print("Está em minúsculo?", nome.islower())
print("Está capitalizada?", nome.istitle())



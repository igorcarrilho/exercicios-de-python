# Refaça o Desafio 9, mostrando a tabuada de um número que o usuário escolher, contudo, utilizando agora
# o laço for
n = int(input('Escolha a tabuada: '))
print(f"TABUADA DO {n}")
print('='*12)
soma = 0
cont = 0
print(f'{n} x {cont} = {n*soma}')
for c in range(0, 10):
    soma = soma + 1
    cont = cont + 1
    print(f'{n} x {cont} = {n*soma}')
print('='*12)
print('FIM')

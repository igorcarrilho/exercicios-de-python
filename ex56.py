# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
idademulher20 = 0
for p in range(1, 5):
    print(f'----- {p} PESSOA -----')
    nome = str(input('NOME: '))
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        idademulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {idademulher20} mulheres com menos de 20 anos')
'''media = idade / 2
    if p == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    print(f'A média da idade dos invivíduos é de {media}')
    print(f'O nome da pessoa mais velha é {nome}')'''
print('FIM')

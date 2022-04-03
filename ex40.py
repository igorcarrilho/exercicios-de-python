# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
# de acordo com a média atingida. Abaixo de 5, reprovado. Entre 5 e 6,9, recuperação. Médi 7 ou superior
# Aprovado
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média é de {media}: REPROVADO')
elif media < 6.9:
    print(f'Sua média é de {media}: RECUPERAÇÃO')
elif media > 7.0:
    print(f'Sua média é de {media}: APROVADO')
print('FIM')

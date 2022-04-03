# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Qual a primeira nota?'))
nota2 = float(input('Qual a segunda nota:'))
media = (nota1 + nota2) / 2
print('A soma média entre {} e {} será {:.1f}'.format(nota1, nota2, media))


# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre a sua categoria com a idade: Até 9 anos-Mirim, até 14 anos, Infantil, até 19 anos, Junior,
# até 25 anos Senior, acima de 25 anos ‘master’
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu:'))
idade = atual - nasc
print(f'Atleta nasceu em {nasc}, portanto tem {idade} anos')
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
print('FIM')

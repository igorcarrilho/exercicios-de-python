# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Ano bissexto não é ano que é somente divisível por 4, mas também anos que são múltiplos de 100 que não
# são múltiplos de 400
# != não igual, diferente
# ano = int(input('Qual ano quer analisar?'))
from datetime import date  # importação para saber a data atual

ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} não é Bissexto!')
else:
    print(f'O ano {ano} não é Bissexto')
print('FIM')

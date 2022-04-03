# Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# de alistamento. O seu programa também deverá mostrar o tempo que falta ou o que passou do prazo
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu?'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos e faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento deveria ter sido em {ano}')
print('FIM')

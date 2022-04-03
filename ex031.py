# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando 50 centavos por Km para viagens de até 200 km e 45 centavos para viagens mais longas
km = float(input('Qual a distância da sua viagem em Km?'))
if km <= 200:
    preco = km * 0.5
    print(f'A sua viagem irá custar R${preco}')
else:
    preco = km * 0.45
    print(f'A sua viagem irá custar R${preco}')
# Método if simplificado
# preco = km * 0.5 if km <= 200 else km * 0.45

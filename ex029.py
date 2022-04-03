# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma
# mesagem dizendo que ele foi multado. A multa vai custar 70 reais por cada km acima do limite
velocidade = float(input('Qual a valocidade atual do carro? '))
print(f'O carro passou a {velocidade} km/h')
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80Km/h!')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança')
print('FIM')

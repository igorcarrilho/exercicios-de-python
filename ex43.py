# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status
# de acordo com: IMC abaixo de 18,5 = abaixo do peso, IMC entre 18.5 e 25 = peso ideal, 20 até 30 = Sobrepeso
# 30 até 40 = Obesidade, acima de 40 = Obesidade mórbida
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, portanto está ABAIXO DO PESO')
elif imc < 25:
    print(f'Seu IMC é de {imc:.1f}, portando está no PESO IDEAL')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.1f}, portanto está com SOBREPESO')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.1f}, portanto está com OBESIDADE')
else:
    print(f'Seu IMC é de {imc:.1f}, portanto está com OBESIDADE MÓRBIDA')
print('FIM')

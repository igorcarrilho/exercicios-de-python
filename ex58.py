# Melhore o jogo do desafio 28 onde o computador vai "pensar" num número entre 0 e 10. Contudo, agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint
computador = randint(0, 10)  # Faz o computador pensar
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez!')
        elif jogador > computador:
            print('Menos... Tente outra vez!')
print(f'Voce acertou com {palpite} tentativas. Parabéns')
print('FIM')

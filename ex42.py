# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triêngulo será formado.
# Equilatero: todos os lados iguais, isósceles: dois lados iguais e um diferente, escaleno: todos os lados
# diferentes
print('+' * 20)
print('Analisador de Triângulos')
print('-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r2 < r1 + r3:
    if r1 == r2 == r3:
        print('Os segmentos acima podem formar um triângulo EQUILATERO')
    elif r1 == r2 or r2 == r3:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES')
    else:
        print('Os segmentos acima podem formar um triângulo ESCALENO')
else:
    print('Os segmentos acima não podem formar um triângulo')
print('FIM')
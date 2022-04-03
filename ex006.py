# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('O dobro de {} vale {}'.format(n, n1))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.3f}'.format(n, n2, n, n3))

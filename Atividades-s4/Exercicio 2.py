"""

Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo
calcule a raiz quadrado do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo
que o número é invalido

"""

from math import sqrt

num = int(input("Digite um número inteiro: "))
rq = int

if num > 0:
    print(f'A raiz quadrada de {num} é {sqrt(num)}')
else:
    print('null number')
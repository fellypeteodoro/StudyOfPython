"""
Exercício 2

Faça um programa que peça para o usuário digitar três valores inteiros e imprima a soma deles.

"""

nome = input("Qual o seu nome? ")
n1: int = int(input('Escolha o 1o número inteiro: '))
n2: int = int(input('Escolha o 2o número inteiro: '))
n3: int = int(input('Escolha o 3o número inteiro: '))
s: int = n1 + n2 + n3
print(f"Muito bem, {nome}, a soma de {n1}, {n2} e {n3} é {s}")
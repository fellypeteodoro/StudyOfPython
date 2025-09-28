"""
Exercício 3

Faça um programa que recebe três vaçpres e apresente a soma dos quadrados dos valores lidos

"""

no = input('Olá, qual é o seu nome? ')
n1: int = int(input("Escolha o 1o número inteiro: "))
n2: int = int(input("Escolha o 2o número inteiro: "))
n3: int = int(input("Escolha o 3o número inteiro: "))

sq: int = (n1*n1) + (n2*n2) + (n3*n3)
print(f"Muito bem, {no}, a soma dos quadrados de {n1}, {n2} e {n3} é {sq}")
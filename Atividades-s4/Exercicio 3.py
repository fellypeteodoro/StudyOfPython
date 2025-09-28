"""

Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar

"""

num = int(input("Escreva um número inteiro: "))

if num%2 == 1:
    print(f'O número {num} é ímpar')
else:
    print(f'O número {num} é par')
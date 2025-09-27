"""
Exercício 1
Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números maiores que 0
"""

cont: int = 0
ind: int = 1

while cont <5:
    if ind % 3 == 0:
        print(f'O número {ind} é multiplo de 3.')
        cont = cont + 1
    ind = ind + 1

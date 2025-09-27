"""

Faça um programa que receba dois números inteiros e mostre qual deles é o maior

"""

n1 = int(input('Informe o primeiro número inteiro: '))
n2 = int(input('Informe o segundo número inteiro: '))
mn = 0

if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}')
elif n2 > n1:
    print(f'O numero {n2} é maior que o número{n1}')
elif n1 == n2:
    print(f'Os números {n1} e {n2} são iguais')

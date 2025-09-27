"""
Loop While

Forma geral:

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso
Exemplo:
num= 5
num > 4
retorna true


"""

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# OBS: Em um loop while é importante que cuidemos/atentemos ao critério de parada.

print('-----------------------------')

# Exemplo 2

resposta = ''

while resposta != 's':
    resposta = input('Ja acabou? [s/n] ')

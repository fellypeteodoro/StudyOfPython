"""

Estruturas de repetição
Loop for
Loop -> É uma estrutura de repetição
For -> Uma dessas estruturas

C ou Java;
for (int i= 0; i < limitador; i++){
    //execução do loop
}

Python;
for item in interavel:
    //execução do loop

Utilizamos loop para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'geek university'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range [1, 10]

"""

nome = 'Geek university'
lista = [1, 3, 5, 7, 9, 14]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)

for letra in nome:
    print(letra)

print('-------------------------------------------')

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

print('-------------------------------------------')

# Exemplo de for 3 (Iterando sobre um range)
"""
Range(valor_inicial, valor_final)
OBS: O valor final não é inclusive. Voce nao inclui o valor final
1, 2, 3, 4, 5, 6, 7, 8, 9, 10-> não
"""
for numero in range(1,10):
    print(numero)

print('-------------------------------------------')

"""
enumerate:

((0, 'g'), (1, 'e'), (2, 'e'), (3, 'k')...)

"""
for indice, letra in enumerate(nome):
    print(nome[indice])

print('-------------------------------------------')

# Quando nao precisamos de um valor, podemos descarta lo com o underline(_)
for _, letra in enumerate(nome):
    print(letra)

print('-------------------------------------------')

for valor in enumerate(nome):
    print(valor[0]) #Somente as os numeros (posiçoes) na posição 0 e letras na posição 1

print('-------------------------------------------')

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd+1): # Colocado mais um pois o range nao vai até o falor final
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

print('-------------------------------------------')

for letra in nome:
    print(letra, end='') # O end serve para nao pular uma linha ao imprimir

print('-------------------------------------------')

# Unicodes...
# Original: U+1F60D
# Modificado: U0001F60D  (Substitui o '+' por três zeros (000))


for num in range(1, 11):
    print('\U0001F60D' * num)
"""
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de
maneira especificada.

Formas gerais:

# Forma 1
range(valor_de_parada)
OBS; valor_de_parada não inclusive(inicio padrão 0, e passo de 1 em 1)

# Forma 2
range(valor_de_inicio, valor_de_parada)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo

# Forma 4 (inversa)
range(valor_de_inicio, valor_de_parada, passo)
"""

# Forma 1 -> passo sera sempre de 1 em 1
for num in range(11): # O valor de parada foi 11, e o inicio padrão foi zero pois nao identifiquei o inicio
    print(num)

print('----------------------------------------')

# Forma 2
for j in range (1, 9):
    print(j)

print('----------------------------------------')

# Forma 3
for p in range(0, 21, 2):
    print(p)

print('----------------------------------------')

# Forma 4
for g in range(50, 0, -5):
    print(g)
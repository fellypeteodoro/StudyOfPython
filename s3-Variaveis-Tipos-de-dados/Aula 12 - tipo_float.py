"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação é '.' e nao ','
"""

# Errado do ponto de vista do Float, mas gera uma tupla

# Valor = 1,44
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

 # É possível fazer uma dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS : Ao converter valores float para inteiro, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com número complexo
variavel = 5j
print(variavel)
print (type(variavel))

"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constanstes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

Sempre com a inicial maiúscula

Errado: true, false
Certo: True, False
"""

# ativo = True
ativo = False

print(ativo)

"""
Operações básicas:
"""
# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso, o resultado será verdadeiro, ou seja, sempre ao contrario
Sempre deve ser escrito em minúsculo
"""
print(not ativo)

"""
'Or' deve sempre ser escrito em minúsculo na operação binária.

True or True -> True
True or False -> True
False or True -> True
False or False -> False

"""

logado = False
print(ativo or logado)

"""
E (and)
Também é uma operação binária, depende de dois valores
Deve ser escrito com letra minúscula (and)

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

print(5 > 6)
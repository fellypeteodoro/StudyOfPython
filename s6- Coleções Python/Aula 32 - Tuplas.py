"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:

1 - As tuplas são representadas por parênteses () (Diferente de listas que são chaves [])
2 - As tuplas são imutáveis: Ao criar uma tupla ela não muda, toda operação em uma tupla gera uma nova tupla


"""

# Exemplo de diferença entre tupla e lista
print(type(()))
print(type([]))

print('-----------------------------')

# CUIDADO 1: As tuplas são representadas por (), mas vemos:

tupla1 = (1, 2, 3, 4, 5, 6)

print(type(tupla1))
print(tupla1)

tupla2 = 1, 2, 3, 4, 5, 6

print(type(tupla2))
print(tupla2)

# Ambos foram considerados tupla, ou seja, com ou sem parenteses, divididos por ',' será formado uma tupla

print('-----------------------------')

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)
print(tupla3)

print(type(tupla3))

# Não foi gerado uma tupla, isso é um número inteiro apenas

tupla4 = (4,) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

# Aqui foi gerado uma tupla, com ',' sendo inserido após um número

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parêntese
# Ela é apresentada com o parenteses mas o que a define é a ','

tupla5 = 1,
print(tupla5)
print(type(tupla5))

# O exemplo acima comprova isso
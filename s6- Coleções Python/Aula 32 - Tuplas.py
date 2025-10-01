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
# (4) -> Não é tupla
# (4,) -> É tupla
# 4, -> É tupla

print('-----------------------------')

# Podemos gerar tupla com range(inicio,fim,passo)

tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))

print('-----------------------------')

# Desempacotamento de tupla

tupla7 = ('Python', 'para', 'desenvolvimento')

tup1, tup2, tup3 = tupla7

print(tup1)
print(tup2)
print(tup3)

print('-----------------------------')

# Métodos para adição e remoção para elementos na tupla não existem, porque elas sao imutáveis.

# Soma*, Valor maximo*, valor mínimo* e Tamanho*:
# Se os valores forem todos inteiros ou reais podemos pegar esses valores

tupla8 = (1, 2, 3, 4, 5, 6)

print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

# ELES DEVEM SER INTEIROS OU REAIS (INT OU FLOAT)

print('-----------------------------')

# Concatenação de tuplas

tupla9 = (1, 2, 3)
print(tupla9)

tupla10 = 4, 5, 6
print(tupla10)

print(tupla9 + tupla10)
print(tupla9)
print(tupla10)

tupla11 = tupla9 + tupla10
print(tupla11)
print(tupla9)
print(tupla10)

tupla9 = tupla9 + tupla10
print(tupla9)
# Tuplas são imutáveis mas podemos sobreescrever seus valores

print('-----------------------------')

# Verificando se determinado elemento está na tupla

tupla12 = 1, 2, 3
print(3 in tupla12)
print(33 in tupla12)

print('-----------------------------')

# Iterando sobre uma tupla

for n, v in enumerate(tupla12):
    print (n, v)

print('-----------------------------')

# Contando elementos dentro de uma tupla

tupla13 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla13.count('a'))
print(tupla13.count('c'))

print('-----------------------------')

# Convertendo string para tupla

escola = tuple('python para desenvolvimento')
print(escola)
print(escola.count('n'))

print('-----------------------------')

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos mudar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')


# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[2])

print('-----------------------------')

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

print('-----------------------------')

# Verificamos em qual indice o elemento esta na tupla
print(meses.index('Junho'))

# Também é possível definir a partir de que indíce ira pesquisar

meses2 = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Junho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro')

print(meses2.index('Junho', 6))
# print(meses2.index('Dezembro', 6, 11)) # Gerra erro pois é do indice 6 ao 11, mas ele esta no '12(-1)
print(meses2.index('Dezembro', 6, 12)) # Forma correta

# Caso o elemento não exista, irá retornar um erro

print('-----------------------------')

# Slicing

# tupla[inicio:fim:passo]

print(meses[0:])
print(meses[5:9]) # Aqui se aplica a regra do i - 1, se quero o indice 8, uso o 9

print('-----------------------------')

# Por que utilizar tuplas?
# 1 - Tuplas são mais rápidas do que listas.
# 2 - Tuplas deixam seu código mais seguro * Porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando tupla para outra

tuplan = 1, 2, 3
print(tuplan)

nova = tuplan # Na tupla não temos o problema de shallow copy

print(tuplan)
print(nova)

outra = 4, 5, 6

nova = nova + outra

print(nova)
print(tuplan)

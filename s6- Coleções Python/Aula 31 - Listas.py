"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays, em ooutras linguagens). com a diferença
de serem DINÂMICO e de podermos colocar QUALQUER tipo de dado.

Linguagens C/JAVA: Arrays
    - Possuem tamanho e tipo de dado fixo;Jum array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar as listas e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dados;

As listas em Python são representadas por colchetes: []

"""
print('-----------------------------')

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 28]

lista2 = ['F', 'e', 'l', 'l', 'y', 'p', 'e', '', 'T', 'e', 'o', 'd', 'o', 'r', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Fellype Teodoro')

#Podemos facilmente checar se determinado valor está contido ná lista
print('Ex 1')
numb= 'jw'
if numb in lista5:
    print(f'Encontrei a letra {numb}')
else:
    print(f'Não encontrei a letra {numb}')
print('-----------------------------')

# Podemos facilmente ordenar uma lista
print('Ex 2')
(lista1.sort())
print(lista1)
print('-----------------------------')

# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print('Ex 3')
print(lista1.count(1))
print(lista5.count('e'))
print('-----------------------------')

# Adicionar elementos em listas
print('Ex 4')
"""
Para adicionar elementos em listas, utilizamos a função append

"""
print(lista1)
lista1.append(42)
print(lista1)

print('-----------------------------')

# OBS: Com append, nós so conseguimos adicioonar 1 elemento por vez
# lista1.append(12, 21, 2) #Vai dar erro

lista1.append([8,3,1])
print(lista1)

if [22,27,27] in lista1:
    print('Encontrei a lista')
else:
    print('Nao encontrei a lista')

print('-----------------------------')

# Se tentar pesquisar 'if 22, 27, 27 in lista1' vai dar falha, apenas é checável
# 1 elemento por vez

#Eles foram adicionados individualmente, diferente do append que necessita das chaves []
# O '.extend' deve ser usado quando for adicionar mais de um elemento
# Se for adicionar somente 1, irá dar falha
lista1.extend([123, 44, 67])
print(lista1)

print('-----------------------------')

# Podemos inserir um novo elemento na lista informando a posição do índice
# Isso nao substitui o valor inicial, o mesmo será deslocado para a direita
lista1.insert(2, 'Novo valor')
print(lista1)

print('-----------------------------')

# Podemos juntar duas listas

#lista6 = lista1 + lista2
# print(lista6)
# lista1.extend(lista2)
# Ou #lista1 = lista1 + lista2
# print(lista1)

print('-----------------------------')

# Imprimindo a lista de forma inversa

# lista1.reverse()
# lista2.reverse()
# ou
# print(lista1[::-1])
# print(lista2[::-1])

# Podemos copiar uma lista

lista6 = lista2.copy()
print(lista6)

print('-----------------------------')

# Contando elementos de uma lista

print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))
print(len(lista5))

print('-----------------------------')

# Podemos remorver o último elemento de uma lista
# OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos a direita desse índice serão deslocados para a esquerda
lista5.pop(2)
print(lista5)

print('-----------------------------')

# Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear()
print(lista5)

print('-----------------------------')

# Repetindo elementos em uma lista
nova = [1, 2, 3]
print(type(nova))
nova = nova * 3
print(nova)

print('-----------------------------')

# Convertendo string para lista
# Exemplo 1
pratica = "estudando python"
print(pratica)
pratica = pratica.split()
print(pratica)
#OBS : Por padrão, o split separa os elementos da lista pelo espaço entre elas

print('-----------------------------')

# Exemplo 2
pratica2 = 'estudando,python,para,desenvolvimento'
print(pratica2)
pratica2 = pratica2.split(',')
print(pratica2)

print('-----------------------------')

# Transformando uma lista novamente em string
lista7 = ['Estudando', 'Python', 'para', 'desenvolvimento']
print(lista7)
# 'PEGUE A LISTA 7, COLOQUE ESPAÇO ENTRE CADA ELEMENTO E TRANSFORME EM STRING'
treino = ' '.join(lista7)
print(treino)

# 'PEGUE A LISTA 7, COLOQUE CIFRÃO ENTRE CADA ELEMENTO E TRANSFORME EM STRING'
treino1 = '$'.join(lista7)
print(treino1)

print('-----------------------------')

# Lista com elementos variados
# Podemos colocar qualquer tipo de dado em uma lista misturando tipos de dados
lista8 = [1, 2, 3.32, True, 'Geek', 'd', [1, 2, 3], 4221]
print(lista8)
print(type(lista8))

print('-----------------------------')

# Iterando sobre listas
# Exemplo 1 - utilizando for

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

print('-----------------------------')


'''
# Exemplo 2 = utilizando while
# Fazendo compras
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

print('A sua lista de compras foi:') 
for produto in carrinho:
    print(produto)

'''

print('-----------------------------')

# Utilizando variáveis em lista

listnum = [1, 2, 3, 4, 5]
print(listnum)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

print('------')

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acessos aos elementos de forma indexidada

#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'preto']
print(cores[0]) # VERDE
print(cores[1]) # AMARELO
print(cores[2]) # AZUL
print(cores[3]) # PRETO

print('-----------------------------')

# Acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, é legal pensar na lista como um círculo!!
# Onde os "--" (-1,-2,-3) andaria em forma anti horária.
print(cores[-1]) # PRETO
print(cores[-2]) # AZUL
print(cores[-3]) # AMARELO
print(cores[-4]) # VERDE
# print(cores[-5]) # ERRO, NÃO EXISTE ÍNDICE -5

print('-----------------------------')

for cor in cores:
    print(cor)

print('-----------------------------')

indice = 0
while indice < len(cores):
    print(cores[indice]) # imprima cores na posição do indice, se eu mudar o indice para 0, a cor verde não aparece
    indice = indice + 1
    print(f'indice em {indice}') # Apenas para ver a logica funcionando 

print('-----------------------------')

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print( indice, cor)

# Acima, quando usamos o 'enumerate', ele faz uma lista como [(0, 'verde'), (1, 'amarelo')]... e assim por diante
# Ao fazer o 'for indice, cor in enumerate(cores)' e pedir para escrever, ele retorna '1 verde', e assim por diante

print('-----------------------------')

# Listas também aceitam valores repetidos
lista10 = []
lista10.append(42)
lista10.append(42)
lista10.append(32)
lista10.append(32)
lista10.append(42)
print(lista10)

print('-----------------------------')

# Outros métodos não tão importantes mas também úteis
# Encontrar o índice de um elemento na lista

produtos = ['ps3', 'ps4', 8, 10, 5, 6, 9, 11, 5]

# Em qual indice está o valor 6
print(produtos.index(6))

# Em qual indice está o valor 'ps4'
print(produtos.index('ps4'))

# OBS: Caso não tenha o elemento na lista, será apresentado "error"
# Exemplo: print(produtos.index('pss4'))

print(produtos.index(5)) # Retorna o indice do 1 elemento encontrado (tendo uma duplicidade)

# Fazendo busca dentro de um range, ou seja, qual indice começar a buscar
print(produtos.index(5, 5)) #Busce o valor '5' apartir do indice 5
"""
PEP8 - PYTHON ENHANCEMENT PROPOSAL

São propostas de melhorias para a linguagem Python

The Zem Of Python

import this

A idéia da PEP8 é que possamos escrever códigos Python de forma Pythônica.
-----------------------------------------------------------------------------
[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCentifica:
    pass
-----------------------------------------------------------------------------
[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis

def soma ():
    pass

def soma_dois():
    pass

numero = 4

numero_impar = 5
-----------------------------------------------------------------------------
[3] - Utilize 4 espaços para identação! (NÃO use tab)

if 'a' in 'banana':
    print('tem')
-----------------------------------------------------------------------------
[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em braco
- Métodos dentro de uma classe devem ser separados com uma única linha em branco
-----------------------------------------------------------------------------
[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado
import sys, os

# Import Certo
import sys
import os

# Não há problemas em utilizar:
from types import StringType, ListType

#Caso tenha muito imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
# e antes de constantes ou variáveis globais
-----------------------------------------------------------------------------
[6] - Espaços em expressões e instruções

# Não faca:

funcao( algo[1], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

#Não Faça

algo (1)

# Faça

algo(1)

# Não Faça

dict ['chave'] = lista [indice]

# Faça

dict['chave'] = lista[indice]

# Não faça:
x              = 1
y              = 3
variavel_longa = 5

# Faça
x = 1
y = 3
variavel_longa = 5

-----------------------------------------------------------------------------
[7] - Termine sempre uma instrução com uma nova linha

# Comentários com varias linhas; iniciar e terminar com tres aspas duplas ou simples
# Comentários com uma linha só; usar o #

# Sempre deixar uma linha após a ultima escrita, se minha ultima linha escrita
# terminar na linha 5, de enter e termine na linha 6
-----------------------------------------------------------------------------
"""
Import this

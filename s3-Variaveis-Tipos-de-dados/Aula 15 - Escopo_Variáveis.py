"""
Escopo de variáveis

Dois casos de escopo

1 - Variáveis globais;
    - Variáveis glovais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja
    seu escopo esta limitado ao bloco onde foi declarada

Para declara variáveis em Python, fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável,
nós nao colocamos o tipo de dado dela, este tipo é inferido ao atribuírmos o valor a mesma.

Exemplo em C:
int numero = 42;

Exemplo em java:
int numero = 42;
"""

numero = 42 # Exemplo de variável global
print(numero, type(numero))

numero = 'geek'
print(numero, type(numero))

# Isso é chamado de reatribuião, reatribui uma outra variável, com o mesmo nome
# com outro tipo de dado, e foi atribuido automaticamente


# Exemplo de variável local
numero = 2

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco if
    print(novo)        # Portanto é local

print(novo)
 # Nesse caso ela é local porque ela pode nao ser definida se a condição não for cumprida
 # Sendo assim ela pode nao ser utilizada

"""

Estruturas Lógicas
And, Or, Not, Is

Operadores unários:
- not, is
Operadores binários:
- and, or
"""

ativo = True
logado = False

# if ativo and logado:
#   print('Bem-vindo, user!')
# else:
#     print("Você precisa ativar sua conta. Por favor cheque seu email!")

if not ativo:
    print("Você precisa ativar sua conta. Por favor cheque seu email!")
else:
    print('Bem-vindo, user!')

# compara um valor com um segundo valor
print(ativo is True)
"""
Recebendo dados do usuário
input() -> todo dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples;           ->  'Pedro'
- Aspas duplas             ->  "Pedro"
- Aspas simples triplas;   ->  '''Pedro'''
"""
# - Aspas duplas  triplas    ->  """Pedro"""

# Entrada de dados
# print("Qual seu nome?")
# nome = input() # Input -> Entrada

nome = input('Qual seu nome? ')

# Exemplo de print antigo (2.x)
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print moderno (3.x)
# print("Seja bem vindo(a) {0}".format(nome))

# Forma mais atual (3.7)
print(f"Seja bem vindo(a) {nome}")

# print("Qual sua idade: ")
# idade = input()

# idade = input("Qual sua idade? ")
idade = int(input("Qual sua idade? "))


# Processamento

# Saída de dados
# Exemplo de print antigo (2.x)
# print("O %s tem %s anos" % (nome, idade))

# Exemplo de print moderno (3.x)
# print("O {0} tem {1} anos".format(nome, idade))

# Forma mais atual (3.7)
print(f"O {nome} tem {idade} anos")

"""
int(idade) => cast
Cast é a conversão de um tipo de dado para outro
"""
# print(f"O {nome} nasceu em {2025 - int(idade)}")
print(f"O {nome} nasceu em {2025 - idade}")
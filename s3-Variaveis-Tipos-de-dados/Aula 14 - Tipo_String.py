"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre apas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

"""
 # - Estiver entre aspas duplas triplas ->  """uma string""", """234""", """a""", """True""", """42.3"""

# O mais comum é aspas simples
#print('True')
#print(type('True'))
#print(True)
#print(type(True))

# Exemplo : nome = Gina's Bar, nesse caso tenho que usar aspas duplas

#nome = "Gina's Bar"
#print(nome)
#print(type(nome))

# Isso irá mandar o 'bar' para a linha de baixo
#nome1 = "Pedro \nAugusto"
#print(nome1)
#print(type(nome1))

#nome2= """ Pedro
#Augusto"""
#print(nome2)
#print(type(nome2))

# Caractere de escápe;
# nome = "Pedro \" Augusto"
# Eu quis colocar aspas mas ja havia aberto a str com aspas, então coloquei
# A barra invertida

nome = 'geek university'
#print(nome.upper())
#print(nome.lower())
# print(nome.split()) - transforma em uma lista de str
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14 ]
# ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']

#print(nome[0:4])  # Slice de string
#print(nome[5:15]) # Slice de string

# [ 0,      1]
# ['Geek', 'University']
#print(nome)print(nome.split())
#print(nome.split()[1])

#print(nome[14], nome[13])

# ::-1 -> começe do primeiro elemento, vá até o ultimo e inverta
print(nome[::-1])
print(nome.replace('e', 'i'))
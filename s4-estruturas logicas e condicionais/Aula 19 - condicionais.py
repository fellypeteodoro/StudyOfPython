"""
Estruturas condicionais
if, else, elif


"""

idade = int(input("Qual é a sua idade?"))

"""
# Estrutura condicional if, em C
if(idade<18){
    printf("Menor de idade");
}else{
    printf("Maior de idade");
}
"""

# Em Python, o bloco após 'if' se inicia com ':', mas é necessário a identação
# Da ação do bloco if, exemplo abaixo:

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade <= 60:
    print('Maior de idade')
else:
    print("Terceira idade")

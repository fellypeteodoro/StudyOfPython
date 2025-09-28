"""
Exercício 2
Faça um programa que utilize o comando while para mostrar na tela uma contagem regressiva, iniciando em 10 e
terminando em 0, MOstre também uma mensagem 'FIM!' após a contagem.

"""

cont : int = 10

while cont >= 0:
    print(cont)
    cont = cont - 1
print('FIM!')
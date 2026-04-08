# 13) Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.
# Imprima os valores em um arquivo.

# Instruções:

# Solicite ao usuário o primeiro número inteiro e armazene-o em uma variável chamada numero1. Solicite ao usuário o segundo número inteiro e
# armazene-o em uma variável chamada numero2. Troque os valores das variáveis numero1 e numero2 utilizando atribuição múltipla.
# Imprima os valores atualizados das variáveis utilizando a função print().

# Digite o primeiro número inteiro: 10
# Digite o segundo número inteiro: 5
# Valores antes da troca: numero1 = 10, numero2 = 5
# Valores depois da troca: numero1 = 5, numero2 = 10

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

print(f"Valores antes da troca: numero1 = {numero1}, numero2 = {numero2}")

numero1, numero2 = numero2, numero1

print(f"Valores depois da troca: numero1 = {numero1}, numero2 = {numero2}")

with open("valores_trocados.txt", "w") as arquivo:
    arquivo.write(f"Valores antes da troca: numero1 = {numero2}, numero2 = {numero1}\n")
    arquivo.write(f"Valores depois da troca: numero1 = {numero1}, numero2 = {numero2}\n")

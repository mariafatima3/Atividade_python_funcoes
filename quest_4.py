# 4) Escreva um programa que solicite ao usuário dois números inteiros e armazene-os em variáveis. Em seguida, calcule e imprima a soma, subtração, multiplicação e
# divisão desses números.


numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))


soma = numero_1 + numero_2
subtracao =numero_1 - numero_2
multiplicacao = numero_1 * numero_2


if numero_2 != 0:
    divisao = numero_1 / numero_2
else:
    divisao = "Erro (divisão por zero)"


print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

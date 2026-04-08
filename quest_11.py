# 11) Escreva um programa que solicite ao usuário dois números e verifique se o primeiro número é maior que o segundo. Imprima uma mensagem informando o resultado da comparação.
# Imprima os valores em um arquivo.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    mensagem = f"O primeiro número ({num1}) é maior que o segundo número ({num2})."
else:
    mensagem = f"O primeiro número ({num1}) não é maior que o segundo número ({num2})."

print(mensagem)

with open("resultado.txt", "w") as arquivo:
    arquivo.write(f"Primeiro número: {num1}\n")
    arquivo.write(f"Segundo número: {num2}\n")
    arquivo.write(f"Resultado da comparação: {mensagem}\n")

print("Os resultados foram salvos em 'resultado.txt'.")

# 9) Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis.
# Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados. Imprima os valores em um arquivo.


valor1 = input("Digite o primeiro valor (True/False): ")
valor2 = input("Digite o segundo valor (True/False): ")

bool1 = valor1.strip().lower() == "true"
bool2 = valor2.strip().lower() == "true"

resultado_and = bool1 and bool2
resultado_or = bool1 or bool2
resultado_not1 = not bool1
resultado_not2 = not bool2

saida = (
    f"Valor 1: {bool1}\n"
    f"Valor 2: {bool2}\n"
    f"AND: {resultado_and}\n"
    f"OR: {resultado_or}\n"
    f"NOT Valor 1: {resultado_not1}\n"
    f"NOT Valor 2: {resultado_not2}\n"
)

print(saida)

with open("resultados.txt", "w") as arquivo:
    arquivo.write(saida)

print("Resultados salvos no arquivo 'resultados.txt'.")

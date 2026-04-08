# 7) Escreva um programa que solicite ao usuário o seu salário mensal e o número de meses trabalhados no ano. Calcule e imprima o salário anual. Imprima os valores em um arquivo.

salario_mensal = float(input("Digite seu sálirio: "))
n_meses_trabalhados_ano = int(input("Digite o número de meses trabalhados no ano: "))

salario_anual = salario_mensal * n_meses_trabalhados_ano

print(f"Salário anual: R$ {salario_anual:.2f}")

with open("salario.txt", "w") as arquivo:
    arquivo.write(f"Salário mensal: R$ {salario_mensal:.2f}\n")
    arquivo.write(f"Meses trabalhados: {n_meses_trabalhados_ano}\n")
    arquivo.write(f"Salário anual: R$ {salario_anual:.2f}\n")

print("Dados salvos no arquivo 'salario.txt'.")



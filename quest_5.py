# 5) Escreva um programa que solicite ao usuário o raio de um círculo e calcule a área e o perímetro desse círculo. Imprima os resultados formatados.Imprima os valores em um arquivo.
import math


raio = float(input("Digite o raio do círculo: "))


area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio


resultado = (
    f"Raio: {raio:.2f}\n"
    f"Área: {area:.2f}\n"
    f"Perímetro: {perimetro:.2f}\n"
)


print("\nResultados:")
print(resultado)


with open("resultado_circulo.txt", "w") as arquivo:
    arquivo.write(resultado)


print("Os resultados foram salvos no arquivo 'resultado_circulo.txt'.")

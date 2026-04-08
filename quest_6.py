# 6) Escreva um programa que solicite ao usuário uma temperatura em graus Celsius e converta-a para Fahrenheit. Imprima o resultado formatado.
# Solicita a temperatura em Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))


fahrenheit = (celsius * 9/5) + 32


print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")

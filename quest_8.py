# 8)Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    
        print(f"O número {numero} é ímpar.")

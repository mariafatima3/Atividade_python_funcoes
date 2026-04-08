# 3) Escreva um programa que solicite ao usuário o seu nome e a sua idade, armazenando esses valores em variáveis.
# Em seguida, imprima uma mensagem formatada mostrando o nome e a idade do usuário. Imprima os valores em um arquivo.


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


mensagem = f"Nome: {nome} | Idade: {idade} anos"


print("\nDados registrados com sucesso:")
print(mensagem)


with open("dados_usuario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(mensagem)


print("\nA mensagem também foi salva no arquivo 'dados_usuario.txt'.")

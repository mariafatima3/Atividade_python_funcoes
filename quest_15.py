# 15) Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch� Time (o número de milessegundos desde 00:00 de 01 de Janeiro de 1970).
# Imprima os valores em um arquivo.

# a) Considere que todos os anos possuem 365 dias

ms_por_dia = 86400000

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

dias = (ano - 1970) * 365

for i in range(mes - 1):
    dias += dias_mes[i]

dias += (dia - 1)

epoch = dias * ms_por_dia

with open("epoch_a.txt", "w") as f:
    f.write(str(epoch))

print("Resultado salvo em epoch_a.txt")



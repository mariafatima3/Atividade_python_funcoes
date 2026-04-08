# b) Considere os anos bissextos:
MS_POR_DIA = 86400000

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

dias_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

dias = 0

for a in range(1970, ano):
    dias += 365
    if bissexto(a):
        dias += 1

if bissexto(ano):
    dias_mes[1] = 29

for i in range(mes - 1):
    dias += dias_mes[i]

dias += (dia - 1)

epoch = dias * MS_POR_DIA

with open("epoch_b.txt", "w") as f:
    f.write(str(epoch))

print("Resultado salvo em epoch_b.txt")

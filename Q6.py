horas = int(input("Quantas horas serão registradas? "))
 
total = 0

i = 1
while i <= horas:
    pecas = int(input("Digite a produção da hora " + str(i) + ": "))
    total = total + pecas
    i = i + 1
 
media = total / horas

print("Produção total:", total, "peças")
print("Média por hora:", media, "peças")
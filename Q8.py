inicio = int(input("Digite o número de início: "))
fim = int(input("Digite o número de fim: "))
 
print("Números pares entre", inicio, "e", fim, "são: ")
 
i = inicio
while i <= fim:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

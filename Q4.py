idade = int(input("Digite sua idade: "))
 
while idade < 0 or idade > 150:
    print("Idade inválida! Digite um valor entre 0 e 150.")
    idade = int(input("Digite sua idade novamente: "))
 
print("Idade digitada:", idade)
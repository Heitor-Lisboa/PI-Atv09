opcao = 0
 
while opcao != 3:
    print("1. Somar dois números")
    print("2. Subtrair dois números")
    print("3. Sair")
 
    opcao = int(input("Escolha uma opção: "))
 
    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", a + b)
 
    if opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", a - b)
 
    if opcao != 1 and opcao != 2 and opcao != 3:
        print("Opção inválida! Tente novamente.")
 
print("Encerrando o programa - - - -")

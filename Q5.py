numero = int(input("Digite um número (0 para encerrar): "))

soma = 0

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número (0 para encerrar): "))
 
print("A soma de todos os números digitados é:", soma)
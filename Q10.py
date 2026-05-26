orcamento = float(input("Digite o orçamento máximo do mês: R$ "))
  
gasto = float(input("Digite um gasto (negativo para encerrar): R$ "))

total_gasto = 0 

while gasto >= 0 and total_gasto + gasto <= orcamento:
    total_gasto = total_gasto + gasto
    print("Gasto registrado! Total gasto até agora: R$", total_gasto)
    gasto = float(input("Digite um gasto (negativo para encerrar): R$ "))
 
if gasto < 0:
    print("Registro encerrado pelo usuário.")
else:
    print("Orçamento excedido! O gasto não foi registrado.")
 
sobrou = orcamento - total_gasto

print("Orçamento:   R$", orcamento)
print("Total gasto: R$", total_gasto)
print("Saldo:       R$", sobrou)
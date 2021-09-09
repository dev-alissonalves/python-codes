from pack import moeda

p = float(input("Digite o preço: R$ "))

print(f"A metade do valor {moeda.conv(p)} é: {moeda.metade(p, True)}")
print(f"O dobro do valor {moeda.conv(p)} é: {moeda.dobro(p, True)}")
print(f"Aumentando 10%, temos: {moeda.aumentar(p, 10, True)}")
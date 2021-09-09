from pack import moeda

p = float(input("Digite o preço: R$ "))

print(f"A metade do valor {moeda.conv(p)} é: {moeda.conv(moeda.metade(p))}")
print(f"O dobro do valor {moeda.conv(p)} é: {moeda.conv(moeda.dobro(p))}")
print(f"Aumentando 10%, temos: {moeda.conv(moeda.aumentar(p, 10))}")
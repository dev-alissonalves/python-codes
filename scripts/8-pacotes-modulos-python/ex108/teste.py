import moeda

p = float(input("Informe um valor qualquer: "))

print("\n")
print("-=-=-=-=- INÍCIO =-=-=-=")
print(f"A metade do valor {p:.2f} é: {moeda.metade(p)}")
print(f"O dobro do valor {p:.2f} é: {moeda.dobro(p)}")
print(f"Aumentando 10%, temos: {moeda.aumentar(p, 10)}")
print(f"Diminuindo 10%, temos: {moeda.diminuir(p, 10)}")
print("-=-=-=-=- FIM =-=-=-=")


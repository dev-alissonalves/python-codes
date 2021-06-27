#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

#modo1
print("============ PROGRESSÃO ARITMÉTICA ============\n")
termo = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão da P.A.: "))
print("\n")
cont = 1
while cont < 11:
    pa = termo + (cont - 1)*razao #fórmula básica da PA
    print(f"{cont}º termo = {pa}")
    cont += 1
print("\n============ PROGRESSÃO ARITMÉTICA ============\n")

#modo2
"""print("============ PROGRESSÃO ARITMÉTICA ============\n")
termo = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão da P.A.: "))
print("\n")

for cont in range (1, 11):
    pa = termo + (cont - 1)*razao #fórmula básica da PA
    print(f"{cont}º termo = {pa}")

print("\n============ PROGRESSÃO ARITMÉTICA ============\n")"""
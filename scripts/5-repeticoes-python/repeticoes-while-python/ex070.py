#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.
total = 0
mil = 0
prod_barato = 0
cont = 0
nome = " "

print("\n--== LOJÃO DO REAL ==--")
while True:
    produto = str(input("Nome do produto: ")).strip().upper()
    valor = float(input("Preço do produto R$:  "))
    cont += 1
    total += valor
    if valor > 1000:
        mil += 1
    if cont == 1 or valor < prod_barato:
        prod_barato = valor
        nome = produto
    op = " "
    while op not in "SN":
        op = str(input("Deseja continuar? [S/N]: " )).strip().upper()[0]
    print("\n")
    if op == "N":
        break

print(f"O total gasto na compra foi R$: {total:.2f}.\n{mil} produto custa mais que R$ 1000.\nO produto mais barato foi a {nome} que custa: {prod_barato}")
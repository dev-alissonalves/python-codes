#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("CAFÉ OURO BRANCO", 2.50, "FEIJÃO PRETO", 9.50, "MANTEIGA DA TERRA", 6.50,"LEITE CONDENSADO", 7.50,"BOLACHA CREAM-CRACKER", 3.50, "HAMBÚRGHER - KG", 8.0,)

print("-"*45)
print(f"{'LISTAGEM DE PREÇOS':^45}")
print("-"*45)
cont = 0
for prod in produtos:
    if cont %2 == 0:   
        print(f"{produtos[cont]:.<30}", end=" ")
    else: 
        print(f"R$: {produtos[cont]:>9.2f}")
    cont += 1

print("-"*45)
print(f"{'FIM PROGRAMA':^45}")
print("-"*45)
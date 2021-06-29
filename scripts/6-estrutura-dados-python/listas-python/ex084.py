#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = []
banco_de_dados = []
maior = 0
menor = 0
print("=======------- CADASTRO VIRTUAL DE SAÚDE -------=======")
print()
while True:
    cadastro.append(str(input("Nome do cidadão: ").strip().upper()))
    cadastro.append(float(input("Informe o peso: ")))
    
    if len(banco_de_dados) == 0:
        maior = menor = cadastro[1]
    else: 
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]

    banco_de_dados.append(cadastro[:])
    cadastro.clear()

    op = ""
    op = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if op == "N":
        break
    print()

print(f"No total tivemos {len(banco_de_dados)} pessaos cadastradas!")
print(f"O maior peso foi de {maior}. Da(s) seguintes pessoa(s): ", end="")
for p in banco_de_dados:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")

print()
print(f"O menor peso foi de {menor}. Da(s) seguintes pessoa(s): ", end="")
for p in banco_de_dados:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
print()

print()
print("=======------- CADASTRO VIRTUAL DE SAÚDE -------=======")
print()
#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoas = dict()
cadastro = list()
soma = media = 0

qtd = 0
while True:
    pessoas["NOME"] = str(input("Informe o seu nome: "))
    while True:
        pessoas["SEXO"] = str(input("SEXO [M/F]: ")).strip().upper()[0]
        if pessoas["SEXO"] in "MF":
            break  
        print("ERRO! Digite apenas M ou F.")
    pessoas["IDADE"] = int(input("IDADE: "))
    soma += pessoas["IDADE"]
    cadastro.append(pessoas.copy())
    qtd += 1
    pessoas.clear()
    op = ""
    while True:
        op = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if op in "SN":
            break
        print("ERRO! Digite apenas S ou N.")
    if op == "N":
        break

print(cadastro)
print(f"A) No total {qtd} pessoa(s) foram cadastradas.")
media = soma/qtd
print(f"B) A média das idades cadastradas é: {media:5.1f} anos")
print("C) Mulheres cadastradas => ", end="")
for p in cadastro:
    if p["SEXO"] == "F":
        print(f"[{p['NOME']}] ", end="")
print()
print("D) Pessoas que estão com a idade acima da média => ", end="")
for p in cadastro:
    if p["IDADE"] >= media:
        print(f"[{p['NOME']}] ", end="")
print("\n")
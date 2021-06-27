# -*- coding: UTF-8 -*-
#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somatorio = 0
idade_homemVelho = 0
nome_homemVelho = ""
qtd_mulheres = 0
print("============ RELATÓRIO SENSO 2021 ============\n")

for cont in range (1, 5):
    nome = str(input(f"NOME DA {cont}º PESSOA: ")).strip().upper()
    idade = int(input(f"IDADE DA {cont}º PESSOA: "))
    sexo = str(input(f"SEXO DA {cont}º PESSOA\n[M OU F]: ")).strip().upper()
    (print("----------------------------"))
    somatorio += idade
    
    if sexo == "F" and idade < 20:
        qtd_mulheres += 1
    
    if cont == 1 and sexo == "M":
        nome_homemVelho = nome
        idade_homemVelho = idade
    else:
        if sexo == "M" and idade > idade_homemVelho:
            nome_homemVelho = nome
            idade_homemVelho = idade

media = somatorio/4
print("\n============ RELATÓRIO SENSO 2021 ============\n")
print(f"\nA média do grupo é: {media}.")
print(f"A quantidade de mulheres menores de 20 anos é: {qtd_mulheres}.")
print(f"O homem mais velho tem {idade_homemVelho} anos e se chama {nome_homemVelho}.\n")
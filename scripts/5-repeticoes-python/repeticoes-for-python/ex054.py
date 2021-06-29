# -*- coding: UTF-8 -*-
#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

print("============ CADASTRO CIDADÃO ============\n")
from datetime import date
ano_atual = date.today().year

ano_pessoa = 0
contadorMaior = 0
contadorMenor = 0
print("INFORME AS DATAS DE NASCIMENTO: ")
for cont in range(1, 8):
    ano_pessoa = int(input(f"DATA DE NASCIMENTO DA {cont}º PESSOA: "))
    if (ano_atual - ano_pessoa) >= 18:
        contadorMaior += 1
    else:
        contadorMenor += 1
print(f"\n[7 PESSOAS CADASTRADAS - RELATÓRIO PARCIAL]\n\033[7;42m--> {contadorMaior} pessoas maiores de idade\033[m\n\033[;41m--> {contadorMenor} pessoas menores de idade\033[m\n\n")
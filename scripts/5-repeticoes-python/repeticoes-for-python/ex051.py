# -*- coding: UTF-8 -*-
#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print("============ PROGRESSÃO ARITMÉTICA ============\n")
termo = int(input("Informe o primeiro termo da P.A.: "))
razao = int(input("Informe a razão da P.A.: "))
print("\n")

for cont in range (1, 11):
    pa = termo + (cont - 1)*razao #fórmula básica da PA
    print(f"{cont}º termo = {pa}")

print("\n============ PROGRESSÃO ARITMÉTICA ============\n")